import heapq
# Common parsing
def parse_input(inputString):
    ship_graph = {} # ship_graph[src] = [(dst, method, cost), ...]
    cost_lookup = {} # cost_lookup[(src, dst, method)] = cost

    if not inputString:
        return ship_graph, cost_lookup
    
    routes = inputString.split(",")
    for route in routes:
        route = route.strip()
        if not route:
            continue
        parts = route.split(":")
        if len(parts) != 4:
            continue # skip if invalid format

        src_country, tgt_country, method, cost_str = parts
        try:
            cost = int(cost_str)
        except ValueError:
            continue # skip if cost is not integer

        ship_graph.setdefault(src_country, []).append(
            (tgt_country, method, cost)
        )
        cost_lookup[(src_country, tgt_country, method)] = cost
    return ship_graph, cost_lookup

# Part 1: give src, dst, method, find cost
def travel_cost(inputString, src_country, tgt_country, method):
    _, cost_lookup = parse_input(inputString)
    cost = cost_lookup.get((src_country, tgt_country, method))
    if cost is None:
        return -1
    return cost

# Part 2: Find route could be directly or at most once mid transfer
def travel_route(inputString, src_country, tgt_country):
    ship_graph, _ = parse_input(inputString)
    if src_country not in ship_graph:
        return None
    
    # first to check directly
    for dst, m, c in ship_graph[src_country]:
        if dst == tgt_country:
            return {
                "route": [src_country, tgt_country],
                "method": [m],
                "cost": c
            }
    
    # then check mid transfer
    for mid, m1, c1, in ship_graph[src_country]:
        if mid not in ship_graph:
            continue
        for dst, m2, c2 in ship_graph[mid]:
            if dst == tgt_country:
                return {
                    "route": [src_country, mid, tgt_country],
                    "method": [m1, m2],
                    "cost": c1 + c2
                }
    return None

# Part 3: continue Part2, find the cheapest
def travel_cheapest(inputString, src_country, tgt_country):
    ship_graph, _ = parse_input(inputString)
    if src_country not in ship_graph:
        return None
    
    best = None # (total_cost, route, methods)

    # All directly
    for dst, m, c in ship_graph[src_country]:
        if dst == tgt_country:
            cand = (c, [src_country, tgt_country], [m])
            if best is None or c < best[0]:
                best = cand
    
    # Mid
    for mid, m1, c1 in ship_graph[src_country]:
        if mid not in ship_graph:
            continue
        for dst, m2, c2 in ship_graph[mid]:
            if dst == tgt_country:
                total = c1 + c2
                cand = (total, [src_country, mid, tgt_country], [m1, m2])
                if best is None or total < best[0]:
                    best = cand

    if best is None:
        return None
    
    total, route, methods = best
    return {
        "route": route,
        "method": methods,
        "cost": total
    }

# Part 4: Cheapest route with any times mid transfer
# Use pq and find by cost, make sure not do the same path to avoid dead cycle
def travel_cheapest_any_transfer(inputString, src_country, tgt_country):
    ship_graph, _ = parse_input(inputString)
    if src_country not in ship_graph:
        return None
    
    # (cost_so_far, node, path, methods)
    heap = [(0, src_country, [src_country], [])]
    vis = set()

    while heap:
        cost, node, path, methods = heapq.heappop(heap)
        if node == tgt_country:
            return {"path": path, "method": methods, "cost": cost}
        
        if (node, len(path)) in vis:
            continue
        vis.add((node, len(path)))
        
        for next, m, c in ship_graph.get(node, []):
            if next in path:
                continue
            heapq.heappush(
                heap,
                (cost + c, next, path + [next], methods + [m])
            )
    return None

# Test
if __name__ == "__main__":
    inputString = "US:UK:FEDEX:5,US:CA:UPS:1,CA:FR:DHL:3,UK:FR:DHL:2,US:FR:UPS:8"

    print("== Q1 basic ==")
    # direct exact match
    print(travel_cost(inputString, "US", "UK", "FEDEX")) # 5
    print(travel_cost(inputString, "US", "FR", "UPS")) # 8
    print(travel_cost(inputString, "US", "FR", "FEDEX")) # -1

    print("\n== Q1 edges ==")
    empty = ""
    print(travel_cost(empty, "US", "UK", "FEDEX")) # -1 
    # invalid segment ignored
    weird = "US:UK:FEDEX:abc,US:UK:FEDEX:7"
    print(travel_cost(weird, "US", "UK", "FEDEX")) # 7

    print("\n== Q2 direct preferred when available ==")
    # direct US->FR:8 exists; should return direct (route length 2)
    r = travel_route(inputString, "US", "FR")
    print(r)  # expect direct route

    print("\n== Q2 one-hop only (no direct) ==")
    only_two_leg = "US:UK:FEDEX:5,UK:FR:DHL:2"
    r = travel_route(only_two_leg, "US", "FR")
    print(r)  # expect cost 7, route ['US','UK','FR']

    print("\n== Q2 unreachable ==")
    unreachable = "US:UK:FEDEX:5,CA:FR:DHL:3"
    print(travel_route(unreachable, "US", "FR"))  # None

    print("\n== Q3 pick the cheapest among direct and one-hop ==")
    # cheapest is US->CA->FR : 1+3=4 (beats direct 8)
    inputString2 = "US:UK:FEDEX:5,US:CA:UPS:1,CA:FR:DHL:3,UK:FR:DHL:2,US:FR:UPS:8"
    print(travel_cheapest(inputString2, "US", "FR"))  # expect cost 4

    print("\n== Q3 tie case (either path is fine if equal) ==")
    same_cost = "US:A:X:3,A:FR:Y:2,US:B:Z:4,B:FR:W:1"  # two routes both 5
    print(travel_cheapest(same_cost, "US", "FR"))  # either route cost=5 acceptable

    print("\n== Q4 multi-hop basic ==")
    chain = "A:B:M1:1,B:C:M2:1,C:D:M3:1,A:D:M4:5"
    print(travel_cheapest_any_transfer(chain, "A", "D"))  # expect cost 3 via A->B->C->D

    print("\n== Q4 with cycle, should not loop ==")
    with_cycle = "A:B:X:1,B:A:Y:1,B:C:Z:10,A:C:W:5"
    print(travel_cheapest_any_transfer(with_cycle, "A", "C"))  # expect cost 5 via direct A->C

    print("\n== Q4 unreachable ==")
    print(travel_cheapest_any_transfer("X:Y:K:1", "A", "B"))  # None

    print("\n== Q4 src==dst (current behavior) ==")
    print(travel_cheapest_any_transfer(chain, "A", "A"))  # None by your current definition