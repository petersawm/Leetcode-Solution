# Part 1: register_receivables
def register_receivables(transactions_csv):
    lines = transactions_csv.strip().splitlines()
    if not lines:
        return []
    data_lines = lines[1:] # skip first (header)
    agg = {} # key:(merchant, card, date) -> amount

    for line in data_lines:
        if not line:
            continue
        parts = line.split(",")
        # c_id = parts[0]
        m_id = parts[1]
        pay_date = parts[2]
        card_type = parts[3]
        amount = int(parts[4])

        key = (m_id, card_type, pay_date)
        agg[key] = agg.get(key, 0) + amount

    receivables = []
    for (m_id, card_type, pay_date), amount in agg.items():
        receivables.append(
            {
                "id": m_id,
                "card_type": card_type,
                "payout_date": pay_date,
                "amount": amount
            }
        )
    return receivables

def print_receivables_for_part1(receivables):
    print("merchant_id,card_type,payout_date,amount")
    for r in receivables:
        print(f"{r['id']},{r['card_type']},{r['payout_date']},{r['amount']}")

# Part 2: update receivables(full buy)
def parse_contracts(contracts_csv): # Parse contract first
    lines = contracts_csv.strip().splitlines()
    if not lines:
        return []
    data_lines = lines[1:]
    res = []

    for line in data_lines:
        if not line:
            continue
        parts = line.split(",")
        c_id = parts[0]
        m_id = parts[1]
        pay_date = parts[2]
        card_type = parts[3]
        amount = int(parts[4])
        res.append(
            {
                "contract_id": c_id,
                "merchant_id": m_id,
                "payout_date": pay_date,
                "card_type": card_type,
                "amount": amount,
            }
        )
    return res

def update_receivables(receivables, contracts_csv):
    contracts = parse_contracts(contracts_csv)
    # key: (merchant_id, card_type, payout_date) -> receivable dict
    rec_map = {}
    for r in receivables:
        key = (r["id"], r["card_type"], r["payout_date"])
        rec_map[key] = r
    
    bought_keys = set()
    new_recs = []
    for c in contracts:
        key = (c["merchant_id"], c["card_type"], c["payout_date"])
        bought_keys.add(key)
        new_recs.append(
            {
                "id": c["contract_id"],
                "card_type": c["card_type"],
                "payout_date": c["payout_date"],
                "amount": c["amount"],
            }
        )
    # not covered
    for key, r in rec_map.items():
        if key not in bought_keys:
            new_recs.append(r)
    return new_recs

def print_receivables_for_part2(receivables):
    print("id,card_type,payout_date,amount")
    for r in receivables:
        print(f"{r['id']},{r['card_type']},{r['payout_date']},{r['amount']}")

# Part 3: Partial buy

def update_receivables_partial(receivables, contracts_csv):
    contracts = parse_contracts(contracts_csv)
    # key: (merchant_id, card_type, payout_date) -> receivable dict
    rec_map = {}
    for r in receivables:
        key = (r["id"], r["card_type"], r["payout_date"])
        rec_map[key] = r
    
    new_rec = []
    # copy: do substract
    for r in receivables:
        new_rec.append(r)
    
    for c in contracts:
        key = (c["merchant_id"], c["card_type"], c["payout_date"])
        rec = rec_map.get(key)
        if rec is not None:
            rec["amount"] -= c["amount"]
            if rec["amount"] < 0:
                rec["amount"] = 0

        new_rec.append(
            {
                "id": c["contract_id"],
                "card_type": c["card_type"],
                "payout_date": c["payout_date"],
                "amount": c["amount"],
            }
        )
    return new_rec

# Test
if __name__ == "__main__":
    print("=== Part 1 ===")

    tx_csv_1 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-30,Visa,150
cust2,merchantA,2021-12-30,Visa,200
cust3,merchantB,2021-12-31,MasterCard,300
cust4,merchantA,2021-12-30,Visa,50
"""
    recs1 = register_receivables(tx_csv_1)
    print_receivables_for_part1(recs1)
    # expect:
    # merchantA,Visa,2021-12-30 -> 150+200+50 = 400
    # merchantB,MasterCard,2021-12-31 -> 300

    print()

    tx_csv_2 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-29,MasterCard,50
cust2,merchantA,2021-12-29,Visa,150
cust3,merchantB,2021-12-31,Visa,300
cust4,merchantB,2021-12-29,MasterCard,200
"""
    recs2 = register_receivables(tx_csv_2)
    print_receivables_for_part1(recs2)
    print()

    print("=== Part 2 ===")

    tx_csv_p2_1 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-05,Visa,300
cust2,merchantA,2022-01-05,Visa,200
cust3,merchantB,2022-01-06,MasterCard,1000
"""
    recs_p2_1 = register_receivables(tx_csv_p2_1)

    contracts_csv_1 = """contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-05,Visa,500
"""
    updated_1 = update_receivables(recs_p2_1, contracts_csv_1)
    print_receivables_for_part2(updated_1)
    # expect:
    # contract1,Visa,2022-01-05,500
    # merchantB,MasterCard,2022-01-06,1000

    print()

    tx_csv_p2_2 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-07,Visa,500
cust2,merchantA,2022-01-07,Visa,250
cust3,merchantB,2022-01-08,MasterCard,1250
cust4,merchantC,2022-01-09,Visa,1500
"""
    recs_p2_2 = register_receivables(tx_csv_p2_2)

    contracts_csv_2 = """contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-07,Visa,750
contract2,merchantC,2022-01-09,Visa,1500
"""
    updated_2 = update_receivables(recs_p2_2, contracts_csv_2)
    print_receivables_for_part2(updated_2)
    # expect:
    # contract1,Visa,2022-01-07,750
    # contract2,Visa,2022-01-09,1500
    # merchantB,MasterCard,2022-01-08,1250

    print()

    print("=== Part 3 (partial) ===")

    tx_csv_p3 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-07,Visa,500
"""
    recs_p3 = register_receivables(tx_csv_p3)

    contracts_csv_p3 = """contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-07,Visa,200
"""
    updated_p3 = update_receivables_partial(recs_p3, contracts_csv_p3)
    print_receivables_for_part2(updated_p3)
    # expect:
    # contract1,Visa,2022-01-07,200
    # merchantA,Visa,2022-01-07,300