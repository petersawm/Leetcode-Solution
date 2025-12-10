# Common parser, return { from_curr: [(to_curr, rate), ...], ... }
def parse_conversion_rates(rates_str):
    if not rates_str:
        return "Error: empty input string"
    
    rate_map = {}
    for entry in rates_str.split(","):
        entry = entry.strip()
        if not entry:
            continue
        parts = entry.split(":")
        if len(parts) != 3: # FROM:TO:RATE
            return f"Error: invalid entry format"
        
        from_curr, to_curr, rate_str = parts
        try:
            rate = float(rate_str)
        except ValueError:
            return f"Error: invalid rate value"
    
        if rate <= 0:
            return f"Error: non positive rate value"
        
        if from_curr not in rate_map:
            rate_map[from_curr] = []
        rate_map[from_curr].append((to_curr, rate))
    
    return rate_map

# Because parser return err str or dict
def _parse_or_error(rates_str):
    p = parse_conversion_rates(rates_str)
    if isinstance(p, str):
        return None, p
    return p, None

def _direct_rates(parsed, from_currency, to_currency):
    return [rate for (to_curr, rate) in parsed.get(from_currency, [])
            if to_curr == to_currency]

# Part 1: get direct conversion rate (from -> to)
def get_direct_conversion_rate(rates_str, from_currency, to_currency):
    parsed, err = _parse_or_error(rates_str)
    if err:
        return err
    rates = _direct_rates(parsed, from_currency, to_currency)
    return rates[0] if rates else "Error: direct conversion not found"

# Part 2: accept 0/1's transfer, return all possible currency list
def get_single_hop_conversion_rate(rates_str, from_currency, to_currency):
    parsed, err = _parse_or_error(rates_str)
    if err:
        return err
    
    rates = []
    # direct from -> to
    rates.extend(_direct_rates(parsed, from_currency, to_currency))
    # one hop: from -> mid -> to
    for mid, r1 in parsed.get(from_currency, []):
        for r2 in _direct_rates(parsed, mid, to_currency):
            rates.append(r1 * r2)
    return sorted(rates) if rates else "Error: no single-hop conversion found"

# Part 3: get best single-hop
def get_best_single_hop_conversion_rate(rates_str, from_currency, to_currency):
    parsed, err = _parse_or_error(rates_str)
    if err:
        return err
    
    best = 0.0
    # direct
    for r in _direct_rates(parsed, from_currency, to_currency):
        best = max(best, r)
    # one hop
    for mid, r1 in parsed.get(from_currency, []):
        for r2 in _direct_rates(parsed, mid, to_currency):
            best = max(best, r1 * r2)
    return best if best > 0 else "Error: no single-hop conversion found"

# Part 4: accept multiple times transfer -> use DFS to find the global optimal
def get_best_conversion_rate(rates_str, from_currency, to_currency):
    parsed, err = _parse_or_error(rates_str)
    if err:
        return err
    
    vis = set()
    max_rate = [0.0]

    def dfs(curr, acc):
        if curr == to_currency:
            max_rate[0] = max(max_rate[0], acc)
            return 
        vis.add(curr)
        for next, rate in parsed.get(curr, []):
            if next not in vis:
                dfs(next, acc * rate)
        vis.remove(curr)
    dfs(from_currency, 1.0)
    return max_rate[0] if max_rate[0] > 0 else "Error: no conversion path found"

# Test
if __name__ == "__main__":
    print("=== Part 1 ===")
    print(get_direct_conversion_rate("AUD:USD:0.7,AUD:JPY:100,USD:CAD:1.2", "AUD", "USD"))
    # Expected: 0.7
    print(get_direct_conversion_rate("AUD:USD:0.7,AUD:JPY:100,USD:CAD:1.2", "AUD", "CAD"))
    # Expected: Error: direct conversion not found
    print(get_direct_conversion_rate("", "AUD", "USD"))
    # Expected: Error: empty input string
    print(get_direct_conversion_rate("AUD:USD:abc", "AUD", "USD"))
    # Expected: Error: invalid rate value
    print(get_direct_conversion_rate("AUD:USD:0.7,AUDJPY100", "AUD", "JPY"))
    # Expected: Error: invalid entry format
    print(get_direct_conversion_rate("aud:usd:0.7", "AUD", "USD"))
    # Expected: Error: direct conversion not found

    print("\n=== Part 2 ===")
    print(get_single_hop_conversion_rate("AUD:USD:0.7,USD:CAD:1.2", "AUD", "USD"))
    # Expected: [0.7]
    print(get_single_hop_conversion_rate("AUD:CAD:0.75,AUD:USD:0.7,USD:CAD:1.2", "AUD", "CAD"))
    # Expected: [0.75, 0.84]
    print(get_single_hop_conversion_rate("AUD:USD:0.7,AUD:EUR:0.6,USD:CAD:1.2,EUR:CAD:1.5", "AUD", "CAD"))
    # Expected: [0.84, 0.9] # multi
    print(get_single_hop_conversion_rate("AUD:JPY:100,USD:CAD:1.2", "AUD", "CAD"))
    # Expected: Error: no single-hop conversion found
    print(get_single_hop_conversion_rate("", "AUD", "USD"))
    # Expected: Error: empty input string
    print(get_single_hop_conversion_rate("AUD:USD:0.7,AUDJPY100", "AUD", "CAD"))
    # Expected: Error: invalid entry format
    print(get_single_hop_conversion_rate("AUD:USD:abc", "AUD", "USD"))
    # Expected: Error: invalid rate value

    print("\n=== Part 3 ===") # 0 or 1 hop, max
    # Two single-hop paths, pick the better one
    print(round(get_best_single_hop_conversion_rate(
        "AUD:USD:0.7,AUD:EUR:0.6,USD:CAD:1.2,EUR:CAD:1.5", "AUD", "CAD"), 2))
    # Expected: 0.9
    print(get_best_single_hop_conversion_rate("AUD:USD:0.7", "AUD", "CAD"))
    # Expected: Error: no single-hop conversion found

    print("\n=== Part 4 ===") # best with any number of hops
    print(get_best_conversion_rate("A:B:2,B:C:2,C:D:2,A:D:5", "A", "D"))
    # Expected: 8.0(A->B->C->D)
    print(get_best_conversion_rate("A:B:2,B:C:2,C:A:0.5,C:D:3", "A", "D"))
    # Expected: 12.0
    print(get_best_conversion_rate("AUD:USD:0", "AUD", "USD"))
    # Expected: Error: non positive rate value
    print(get_best_conversion_rate("AUD:USD:-1.2", "AUD", "USD"))
    # Expected: Error: non positive rate value