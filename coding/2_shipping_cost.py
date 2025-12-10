def _get_country_and_items(order: dict):
    country = order.get("country")
    items = order.get("items") or []
    if not country:
        return None, None, "ERR_COUNTRY"
    return country, items, None

def _build_product_index(country_cost_list: list):
    # e.g. [{"product":"mouse",...}, {"product":"laptop",...}] 
    # => {"mouse": {...}, "laptop": {...}}
    return {e["product"]: e for e in country_cost_list}

def _apply_tiers(qty: int, tiers: list, allow_fixed: bool):
    # ensure tier data will not mess
    tiers = sorted(tiers, key=lambda t: t.get("minQuantity", 0))
    rem, subtotal = qty, 0
    for t in tiers:
        if rem <= 0:
            break
        min_q = t.get("minQuantity", 0)
        max_q = t.get("maxQuantity", None)
        c = t.get("cost")
        if c is None:
            return "ERR_TIER"
        use = rem if max_q is None else max(0, min(rem, max_q - min_q))
        if use <= 0:
            continue
        if allow_fixed and t.get("type", "incremental") == "fixed":
            subtotal += int(c) # fixed
        else:
            subtotal += use * int(c) # incremental
        rem -= use
    return subtotal

# Part 1: fixed -> qty * cost
def calculate_shipping_cost_part1(order: dict, shipping_cost: dict):
    country, items, err = _get_country_and_items(order)
    if err or country not in shipping_cost:
        return "ERR_COUNTRY"

    idx = _build_product_index(shipping_cost[country])
    total = 0
    for it in items:
        p = it.get("product")
        q = it.get("quantity", 0)
        if not p or q <= 0:
            continue
        cfg = idx.get(p)
        if not cfg:
            return "ERR_NOT_FOUND"   
        c = cfg.get("cost")     
        total += q * int(c)
    return total

# Part 2: incremental
def calculate_shipping_cost_part2(order: dict, shipping_cost: dict):
    country, items, err = _get_country_and_items(order)
    if err or country not in shipping_cost:
        return "ERR_COUNTRY"

    idx = _build_product_index(shipping_cost[country])
    total = 0
    for it in items:
        p = it.get("product")
        q = it.get("quantity", 0)
        if not p or q <= 0:
            continue
        cfg = idx.get(p)
        if not cfg:
            return "ERR_NOT_FOUND"
        tiers = cfg.get("costs")
        if not tiers:
            return "ERR_CFG" 
        sub = _apply_tiers(q, tiers, allow_fixed=False)
        if isinstance(sub, str):
            return sub               # 传递 ERR_TIER
        total += sub
    return total

# Part 3: type（fixed / incremental）
def calculate_shipping_cost_part3(order: dict, shipping_cost: dict):
    country, items, err = _get_country_and_items(order)
    if err or country not in shipping_cost:
        return "ERR_COUNTRY"

    idx = _build_product_index(shipping_cost[country])
    total = 0
    for it in items:
        p = it.get("product")
        q = it.get("quantity", 0)
        if not p or q <= 0:
            continue
        cfg = idx.get(p)
        if not cfg:
            return "ERR_NOT_FOUND"

        tiers = cfg.get("costs")
        if not tiers:
            c = cfg.get("cost")
            if c is None:
                return "ERR_CFG"
            total += q * int(c)
            continue

        sub = _apply_tiers(q, tiers, allow_fixed=True)
        if isinstance(sub, str):
            return sub
        total += sub
    return total

# Test
if __name__ == "__main__":
    order_us = {
        "country": "US",
        "items": [
            {"product": "mouse", "quantity": 20},
            {"product": "laptop", "quantity": 5},
        ],
    }
    order_ca = {
        "country": "CA",
        "items": [
            {"product": "mouse", "quantity": 20},
            {"product": "laptop", "quantity": 5},
        ],
    }

    # ---- Part 1 测试（固定单价）----
    shipping_p1 = {
        "US": [
            {"product": "mouse", "cost": 550},
            {"product": "laptop", "cost": 1000},
        ],
        "CA": [
            {"product": "mouse", "cost": 750},
            {"product": "laptop", "cost": 1100},
        ],
    }
    print("Part 1")
    print("US:", calculate_shipping_cost_part1(order_us, shipping_p1))  # 16000
    print("CA:", calculate_shipping_cost_part1(order_ca, shipping_p1))  # 20500

    # ---- Part 2 测试（阶梯 incremental）----
    shipping_p2 = {
        "US": [
            {
                "product": "mouse",
                "costs": [
                    {"minQuantity": 0, "maxQuantity": None, "cost": 550},
                ],
            },
            {
                "product": "laptop",
                "costs": [
                    {"minQuantity": 0, "maxQuantity": 2, "cost": 1000},
                    {"minQuantity": 3, "maxQuantity": None, "cost": 900},
                ],
            },
        ],
        "CA": [
            {
                "product": "mouse",
                "costs": [
                    {"minQuantity": 0, "maxQuantity": None, "cost": 750},
                ],
            },
            {
                "product": "laptop",
                "costs": [
                    {"minQuantity": 0, "maxQuantity": 2, "cost": 1100},
                    {"minQuantity": 3, "maxQuantity": None, "cost": 1000},
                ],
            },
        ],
    }
    print("\nPart 2")
    print("US:", calculate_shipping_cost_part2(order_us, shipping_p2))  # 15700
    print("CA:", calculate_shipping_cost_part2(order_ca, shipping_p2))  # 20200

    # ---- Part 3 测试（fixed + incremental）----
    shipping_p3 = {
        "US": [
            {
                "product": "mouse",
                "costs": [
                    {
                        "type": "incremental",
                        "minQuantity": 0,
                        "maxQuantity": None,
                        "cost": 550,
                    }
                ],
            },
            {
                "product": "laptop",
                "costs": [
                    {
                        "type": "fixed",
                        "minQuantity": 0,
                        "maxQuantity": 2,
                        "cost": 1000,
                    },
                    {
                        "type": "incremental",
                        "minQuantity": 3,
                        "maxQuantity": None,
                        "cost": 900,
                    },
                ],
            },
        ],
        "CA": [
            {
                "product": "mouse",
                "costs": [
                    {
                        "type": "incremental",
                        "minQuantity": 0,
                        "maxQuantity": None,
                        "cost": 750,
                    }
                ],
            },
            {
                "product": "laptop",
                "costs": [
                    {
                        "type": "fixed",
                        "minQuantity": 0,
                        "maxQuantity": 2,
                        "cost": 1100,
                    },
                    {
                        "type": "incremental",
                        "minQuantity": 3,
                        "maxQuantity": None,
                        "cost": 1000,
                    },
                ],
            },
        ],
    }
    print("\nPart 3")
    print("US:", calculate_shipping_cost_part3(order_us, shipping_p3))  # 14700
    print("CA:", calculate_shipping_cost_part3(order_ca, shipping_p3))  # 19100

    print("\nExtra checks (US laptop only, Part 3 tiers):")
    for q in [1, 2, 3, 4]:
        test_order = {"country": "US", "items": [{"product": "laptop", "quantity": q}]}
        print(f"qty={q}: ", calculate_shipping_cost_part3(test_order, shipping_p3))
        # 1 -> 1000 (fixed)
        # 2 -> 1000 (fixed)
        # 3 -> 1900 (1000 + 1*900)
        # 4 -> 2800 (1000 + 2*900)

# def calculate_shipping_cost(order, shipping_cost):
#     country = order.get("country")
#     if not country:
#         return "Error: country missing"
    
#     items = order.get("items") or order.get("product") or []

#     c_costs = shipping_cost.get(country)
#     if c_costs is None:
#         return f"Error: country '{country}' not in shipping_cost"
    
#     # product -> correspoding stuffs
#     p_map = {p["product"]: p for p in c_costs}
#     total = 0

#     for it in items:
#         name = it.get("product")
#         qty = it.get("quantity", 0)

#         if not name or qty <= 0:
#             continue

#         info = p_map.get(name)
#         if info is None:
#             return f"Error: product '{name}' not in shipping_cost for {country}"
        
#         # Part 1: flat cost
#         if "cost" in info and "costs" not in info:
#             total += qty * info["cost"]
#             continue

#         # Part2/3: tiered costs
#         if "costs" not in info:
#             return f"Error: no 'cost' or 'costs' for product '{name}'"
        
#         tiers = info["costs"]
#         if not tiers:
#             return f"Error: empty costs for product '{name}'"
        
#         # sorted by minQuantity
#         tiers = sorted(tiers, key=lambda t: t["minQuantity"])

#         rem = qty
        
#         for t in tiers:
#             min_q = t.get("minQuantity", 0)
#             max_q = t.get("maxQuantity", None)
#             tier_cost = t.get("cost")
#             t_type = t.get("type", "incremental") # default: incremental

#             if tier_cost is None:
#                 return f"Error: missing cost in tier for product '{name}'"
            
#             # calculate how many could be covered
#             if max_q is None:
#                 use = rem
#             else:
#                 cap = max_q - min_q
#                 if cap < 0:
#                     cap = 0
#                 use = min(rem, cap)
            
#             if use <= 0:
#                 continue

#             if t_type == "incremental":
#                 total += use * tier_cost
#             elif t_type == "fixed":
#                 total += tier_cost
#             else:
#                 return f"Error: unknown cost type '{t_type}'"
            
#             rem -= use
#             if rem <= 0:
#                 break

#     return total