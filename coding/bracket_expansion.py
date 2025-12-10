# Helper
def _find_single_brace_pair(s: str):
    l = s.find("{")
    if l == -1:
        return -1, -1
    r = s.find("}", l + 1)
    if r == -1 or r < l:
        return -1, -1
    first_close = s.find("}")
    if first_close != -1 and first_close < l:
        return -1, -1
    return l, r

# Part 1: expand single valid brace
def expand_single_brace_part1(s: str):
    l, r = _find_single_brace_pair(s)
    if l == -1:
        return [s] # no match
    inside = s[l + 1: r]
    tokens = [t for t in inside.split(",") if t != ""]
    if len(tokens) < 2:
        return [s]
    
    prefix = s[:l]
    suffix = s[r + 1:]
    return [prefix + t + suffix for t in tokens]

# Part 2: don't expand if invalid
def expand_single_brace_part2(s: str):
    l, r = _find_single_brace_pair(s)
    if l == -1:
        return [s]
    inside = s[l + 1: r]
    raw = inside.split(",")
    tokens = [t for t in raw if t != ""]
    if len(tokens) < 2:
        return [s]
    
    prefix = s[:l]
    suffix = s[r + 1:]
    return [prefix + t + suffix for t in tokens]
    
# Part 3: similar to lc 1087
def brace_expansion(s):
    seg = []
    i, n = 0, len(s)
    literal = []

    while i < n:
        if s[i] != "{":
            literal.append(s[i])
            i += 1
            continue
        # flush literal before a brace
        if literal:
            seg.append(["".join(literal)])
            literal = []

        j = i + 1 # find "}"
        while j < n and s[j] != "}":
            j += 1
        if j == n:
            literal.append(s[i:])
            i = n
            break

        inside = s[i + 1:j]
        opts = [t for t in inside.split(",") if t != ""]
        if not opts:
            literal.append(s[i:j + 1])
        else:
            opts.sort()
            seg.append(opts)
        i = j + 1 # skip cur pair
    
    if literal:
        seg.append(["".join(literal)])
    if not seg:
        return [s]
    
    res = []

    def dfs(idx: int, path: str):
        if idx == len(seg):
            res.append(path)
            return
        for opt in seg[idx]:
            dfs(idx + 1, path + opt)
    
    dfs(0, "")
    return res

# Test
if __name__ == "__main__":
    print("=== Part 1 (basic single brace) ===")
    s1 = "/2022/{jan,feb,march}/report"
    print(expand_single_brace_part1(s1))
    # Expected:
    # ["/2022/jan/report", "/2022/feb/report", "/2022/march/report"]

    print(expand_single_brace_part1("pre{mid}suf"))  # ["pre{mid}suf"]
    print(expand_single_brace_part1("pre{}suf"))     # ["pre{}suf"]
    print(expand_single_brace_part1("premidsuf"))    # ["premidsuf"]

    print("\n=== Part 2 (strict invalid handling) ===")
    print(expand_single_brace_part2(s1))
    # Expected:
    # ["/2022/jan/report", "/2022/feb/report", "/2022/march/report"]

    print(expand_single_brace_part2("pre{mid}suf"))  # ["pre{mid}suf"]
    print(expand_single_brace_part2("pre{}suf"))     # ["pre{}suf"]
    print(expand_single_brace_part2("pre}abc{xyz"))  # ["pre}abc{xyz"]
    print(expand_single_brace_part2("pre{a,,}suf"))  # ["pre{a,,}suf"]
    print(expand_single_brace_part2("pre{a,b}suf"))  # ["preasuf","prebsuf"]

    print("\n=== Part 3 (multi-brace expansion / LC1087 style) ===")
    print(brace_expansion("{a,b}c{d,e}f"))
    # Expected: ["acdf","acef","bcdf","bcef"]

    print(brace_expansion("/2022/{jan,feb}/{x,y}/report"))
    # Expected:
    # /2022/jan/x/report
    # /2022/jan/y/report
    # /2022/feb/x/report
    # /2022/feb/y/report

    print(brace_expansion("pre{a,b,c}suf"))
    # Expected: ["preasuf", "prebsuf", "precsuf"]