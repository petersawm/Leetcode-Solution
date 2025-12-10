# Common: parse requests, return list[dict] sorted by time
def parse_payments(requests):
    payments = []
    for req in requests.split("\n"):
        line = req.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 5:
            # skip header if it's not digit, because input is csv
            f = parts[0].strip()
            if not f.isdigit():
                continue
            continue # invalid format

        ts_str, unique_id, amount, card_number, merchant = parts
        # timestamp -> int
        if not ts_str.strip().isdigit():
            continue

        payments.append(
            {
                "timestamp_seconds": int(ts_str),
                "unique_id": unique_id,
                "amount": amount,
                "card_number": card_number,
                "merchant": merchant
            }
        )
    # sort
    payments.sort(key=lambda x: x["timestamp_seconds"])
    return payments

# Part 1: all approve
def validate_authorization_report(requests):
    payments = parse_payments(requests)
    for p in payments:
        output = (
            f"{p['timestamp_seconds']} "
            f"{p['unique_id']} "
            f"{p['amount']} "
            f"APPROVE"
        )
        print(output)

# Helper: parse rules
def parse_rules(requests_rules):
    rules = []
    for req in requests_rules.split("\n"):
        line = req.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 3:
            f = parts[0].strip() # skip header
            if not f.isdigit():
                continue
            continue

        ts_str, field, value = parts
        if not ts_str.strip().isdigit():
            continue

        rules.append(
            {
                "timestamp_seconds": int(ts_str),
                "field": field,
                "value": value
            }
        )
    rules.sort(key=lambda x: x["timestamp_seconds"])
    return rules

# Part 2: apply rules -> REJECT/APPROVE
# check all time <= req.time
def apply_fraud_rules(requests_payments, requests_rules):
    payments = parse_payments(requests_payments)
    rules = parse_rules(requests_rules)

    for p in payments:
        t = p["timestamp_seconds"]
        is_approved = True
        for r in rules:
            if r["timestamp_seconds"] > t:
                break

            field = r["field"]
            value = r["value"]
            if value == p[field]:
                is_approved = False # Reject
                break

        output = (
            f"{p['timestamp_seconds']} "
            f"{p['unique_id']} "
            f"{p['amount']} "
        )

        if is_approved:
            output += "APPROVE"
        else:
            output += "REJECT"
        print(output)

# Part 3: fraud loss(prev approve, but hit the rules later)
def cal_total_fraud_loss(requests_payments, requests_rules):
    payments = parse_payments(requests_payments)
    rules = parse_rules(requests_rules)

    total = 0.0
    for p in payments:
        t = p["timestamp_seconds"]
        # first check if it should be rejected at prev time
        rej_at_time = False
        for r in rules:
            if r["timestamp_seconds"] > t:
                break
            field = r["field"]
            value = r["value"]
            if value == p[field]:
                rej_at_time = True
                break
        if rej_at_time: 
            # we don't incl the rej in loss cuz money didn't pay out
            continue
        # check if it hits fraud for later rules
        for r in rules:
            if r["timestamp_seconds"] > t:
                field = r["field"]
                value = r["value"]
                if value == p[field]:
                    total += float(p["amount"])
                    break
    print("Total fraud loss:", total)

# Test
if __name__ == "__main__":
    print("***** Part 1 *****")
    # Edge 1: 多条、时间无序
    data1 = """5,R1,5.60,4242424242424242,bobs_burgers
10,R2,500.00,4242111111111111,a_corp
3,R3,12.00,4111111111111111,coffee_shop
7,R4,100.00,4000000000000000,hardware_store"""
    validate_authorization_report(data1)
    # 期望输出顺序：3, 5, 7, 10，全部 APPROVE

    print("\n***** Part 1 - single row *****")
    data2 = "8,R8,42.00,4012888888881881,sushi_place"
    validate_authorization_report(data2)
    # 期望：8 R8 42.00 APPROVE

    print("\n***** Part 2 *****")
    # Edge 1: 规则在请求之前，命中 merchant
    data_p2_1 = """5,R1,5.60,4242,bobs_burgers
10,R2,100.00,4242,a_corp"""
    rules_p2_1 = "1,merchant,bobs_burgers"
    # 期望：
    # 5 R1 5.60 REJECT
    # 10 R2 100.00 APPROVE
    apply_fraud_rules(data_p2_1, rules_p2_1)

    # Edge 2: 规则在请求之后 -> 只影响未来，当前不 REJECT
    print("\n***** Part 2 - rule comes after *****")
    data_p2_2 = """5,R1,5.60,4242,bobs_burgers
10,R2,100.00,4242,a_corp"""
    rules_p2_2 = "6,merchant,bobs_burgers"
    # 期望（实时）：当时没有生效 -> 都 APPROVE
    apply_fraud_rules(data_p2_2, rules_p2_2)

    # Edge 3: card_number 介于两次请求之间变 fraud
    print("\n***** Part 2 - card becomes fraud between requests *****")
    data_p2_3 = """10,R1,10.00,1234,a
20,R2,20.00,1234,a
30,R3,30.00,1234,a"""
    rules_p2_3 = "25,card_number,1234"
    # 期望实时结果：
    # 10 R1 10.00 APPROVE
    # 20 R2 20.00 APPROVE
    # 30 R3 30.00 REJECT
    apply_fraud_rules(data_p2_3, rules_p2_3)

    print("\n***** Part 2 - multiple rules *****")
    data_p2_4 = """10,X1,9.00,9999,safe_store
15,X2,9.00,8888,safe_store
20,X3,9.00,7777,fraud_store"""
    rules_p2_4 = """12,card_number,8888
19,merchant,fraud_store"""
    # 期望：
    # 10 X1 9.00 APPROVE
    # 15 X2 9.00 REJECT       (card_number 8888 从 t=12 起 fraud)
    # 20 X3 9.00 REJECT       (merchant fraud_store 从 t=19 起 fraud)
    apply_fraud_rules(data_p2_4, rules_p2_4)

    print("\n***** Part 3 - basic fraud loss *****")
    # 示例：当时都 APPROVE，但之后才有规则
    data_p3_1 = """5,R1,5.60,4242,bobs_burgers
10,R2,100.00,4242,a_corp"""
    rules_p3_1 = """20,card_number,4242
30,merchant,bobs_burgers"""
    # 期望 fraud loss = 5.6 + 100.0 = 105.6
    cal_total_fraud_loss(data_p3_1, rules_p3_1)

    print("\n***** Part 3 - immediate reject, no loss *****")
    # 这里 merchant 从一开始就是 fraud
    data_p3_2 = "10,R1,100.00,1234,bobs_burgers"
    rules_p3_2 = """1,merchant,bobs_burgers
20,card_number,1234"""
    # 当时就被 rule1 (t=1) 拦下 -> 不算 loss
    # 即使 20 秒有 rule2 命中同一笔交易，也不再算损失
    cal_total_fraud_loss(data_p3_2, rules_p3_2)
    