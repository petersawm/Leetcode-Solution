def parse_payment_with_invoice(s):
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 4:
        return None
    pid, amt_str, memo, iid = parts
    return {
        "pid": pid,
        "amount_str": amt_str,
        "amount": float(amt_str),
        "memo": memo,
        "invoice_id": iid,
    }

# use for part 2 and 3
def parse_payment_no_invoice(s):
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 3:
        return None
    pid, amt_str, memo = parts
    return {
        "pid": pid,
        "amount_str": amt_str,
        "amount": float(amt_str),
        "memo": memo,
    }

def parse_invoice(s):
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 3:
        return None
    iid, due, amt_str = parts
    return {
        "iid": iid,
        "due": due,
        "amount_str": amt_str, # "YYYY-MM-DD"
        "amount": float(amt_str),
    }

# Part 1: payment incl invoiceId, find due date with this
def payment_statement_v1(payment_str, invoice_list):
    pay = parse_payment_with_invoice(payment_str)
    if not pay:
        return "invalid payment input"
    
    iid = pay["invoice_id"]
    match_inv = None
    for inv_s in invoice_list:
        inv = parse_invoice(inv_s)
        if not inv:
            continue
        if inv["iid"] == iid:
            match_inv = inv
            break
    
    if not match_inv:
        return f"{pay['pid']} has no matching invoice {iid}"
    return f"{pay['pid']} paid off by {iid} due on {match_inv['due']}"

# helper: find amt == payment.amt with earliest due date
def find_invoice_exact_by_amount(payment, invoice_list):
    tgt_amt = payment["amount"]
    best = None # (due, invoice_dict)
    for inv_s in invoice_list:
        inv = parse_invoice(inv_s)
        if not inv:
            continue
        if inv["amount"] == tgt_amt:
            if best is None or inv["due"] < best[0]:
                best = (inv["due"], inv)
    return best[1] if best else None

# Part 2: will not give "invoice_id"
def payment_statement_v2(payment_str, invoice_list):
    pay = parse_payment_no_invoice(payment_str)
    if not pay:
        return "invalid payment input"
    
    inv = find_invoice_exact_by_amount(pay, invoice_list)
    if not inv:
        return f"{pay['pid']} has no invoice with exact amount {pay['amount_str']}"
    
    return (
        f"{pay['pid']} paid off by {inv['iid']} "
        f"due on {inv['due']} by {pay['amount_str']}"
    )

# helper: find abs(inv.amt - payment,amt) <= amt_range
def find_invoice_in_range(payment, invoice_list, amt_range):
    tgt_amt = payment["amount"]
    best = None
    
    for inv_s in invoice_list:
        inv = parse_invoice(inv_s)
        if not inv:
            continue
        if abs(inv["amount"] - tgt_amt) <= amt_range:
            if best is None or inv["due"] < best[0]:
                best = (inv["due"], inv)
    return best[1] if best else None

# Part 3: add range
def payment_statement_v3(payment_str, invoice_list, amt_range):
    pay = parse_payment_no_invoice(payment_str)
    if not pay:
        return "invalid payment input"
    # exact match first
    inv = find_invoice_exact_by_amount(pay, invoice_list)
    if inv:
        return (
            f"{pay['pid']} paid off by {inv['iid']} "
            f"due on {inv['due']} by {pay['amount_str']}"
        )
    # try range
    inv = find_invoice_in_range(pay, invoice_list, amt_range)
    if inv:
        return (
            f"{pay['pid']} paid off by {inv['iid']} "
            f"due on {inv['due']} by {pay['amount_str']}"
        )
    
    return (
        f"{pay['pid']} has no invoice within range "
        f"+-{amt_range} around {pay['amount_str']}"
    )

# Test
if __name__ == "__main__":
    print("===== Part 1 =====")
    payment1 = "paymentX,600,Paying off: invoiceX,invoicex"
    invoices1 = [
        "invoicea,2024-03-22,100",
        "invoiceb,2024-02-05,400",
        "invoicex,2025-05-20,1000",
    ]
    print(payment_statement_v1(payment1, invoices1))
    # exp：paymentX paid off by invoicex due on 2025-05-20

    print("\n===== Part 2 =====")
    payment2 = "paymentY,600,Some memo"
    invoices2 = [
        "invoicea,2024-03-22,100",
        "invoiceb,2024-02-05,600",   # should hit
        "invoicec,2025-05-20,600",   # later due
    ]
    print(payment_statement_v2(payment2, invoices2))
    # exp：paymentY paid off by invoiceb due on 2024-02-05 by 600

    print("\n===== Part 3 =====")
    payment3 = "paymentZ,500,Pay something"
    invoices3 = [
        "inv1,2024-01-01,480",     
        "inv2,2024-01-05,500",      # exact match
        "inv3,2023-12-31,520",     
    ]
    # range=50
    print(payment_statement_v3(payment3, invoices3, 50))
    # exp：paymentZ paid off by inv2 due on 2024-01-05 by 500

    print("\n===== Part 3 =====")
    payment4 = "paymentW,500,No exact"
    invoices4 = [
        "inv10,2024-02-01,460",    # diff=40，in range
        "inv11,2024-01-20,470",    # diff=30，in due, early due -> should select this
        "inv12,2024-03-01,700",    # out of range
    ]
    print(payment_statement_v3(payment4, invoices4, 50))
    # exp: paymentW paid off by inv11 due on 2024-01-20 by 500

    print("\n===== Part 3=====")
    payment5 = "paymentQ,1000,big payment"
    invoices5 = [
        "ia,2024-01-01,100",
        "ib,2024-01-02,200",
    ]
    print(payment_statement_v3(payment5, invoices5, 50))
    # exp: no invoice within range