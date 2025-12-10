# Part 1: give log and closing_time, calculate penalty
# Open && N -> +1 / Close && Y -> +1
def compute_penalty(log, closing_time):
    if not log:
        return 0
    customers = log.split(" ")
    penalty = 0
    for i in range(len(customers)):
        c = customers[i]
        if i < closing_time:
            if c == "N":
                penalty += 1
        else:
            if c == "Y":
                penalty += 1
    return penalty

# Part 2: find min closing_time
# go through each hour, Y -> penalty -= 1; N -> penalty += 1
def find_best_closing_time(log):
    if not log:
        return 0
    customers = log.split(" ")
    penalty, min_penalty, min_idx = 0, 0
    for i in range(len(customers)):
        if customers[i] == "Y":
            penalty -= 1
        else:
            penalty += 1
        if penalty < min_penalty:
            min_penalty = penalty
            min_idx = i + 1
    return min_idx

# Part 3: no nested
def get_best_closing_times(aggregate_log):
    tokens = aggregate_log.split()
    res = []
    in_log = False # whether in BEGIN...END
    bad = False # check if log is invalid(nested BEGIN or invalid token)
    cur = []
    for t in tokens:
        if t == "BEGIN":
            if not in_log:
                in_log = True
                bad = False
                cur = []
            else:
                bad = True
        elif t == "END":
            if in_log:
                if not bad:
                    log_str = " ".join(cur)
                    best = find_best_closing_time(log_str) if log_str else 0
                    res.append(best)
                in_log = False
                bad = False
                cur = []
            else:
                continue
        else:
            if in_log and not bad:
                if t in ("Y", "N"):
                    cur.append(t)
                else:
                    bad = True
    return res

# Part 4: input: file, streaming read
def get_best_closing_times_v2(filename):
    res = []
    in_log = False
    bad = False
    cur = []
    with open(filename, "r") as f:
        for line in f:
            tokens = line.split()
            for t in tokens:
                if t == "BEGIN":
                    if not in_log:
                        in_log = True
                        bad = False
                        cur = []
                    else:
                        bad = True
                elif t == "END":
                    if in_log:
                        if not bad:
                            log_str = " ".join(cur)
                            best = find_best_closing_time(log_str) if log_str else 0
                            res.append(best)
                        in_log = False
                        bad = False
                        cur = []
                    else:
                        continue
                else:
                    if in_log and not bad:
                        if t in ("Y", "N"):
                            cur.append(t)
                        else:
                            bad = True
    return res

# Test
if __name__ == "__main__":
    print("Part 1:")
    print("Case 1:", compute_penalty("Y Y N Y", 0))   # 3
    print("Case 2:", compute_penalty("N Y N Y", 2))   # 2
    print("Case 3:", compute_penalty("Y Y N Y", 4))   # 1
    print("Edge 1:", compute_penalty("", 0))          # 0
    print("Edge 2:", compute_penalty("N N N N", 0))   # 0
    print("Edge 3:", compute_penalty("Y Y Y Y", 4))   # 0
    print("Edge 4:", compute_penalty("Y N Y N", 2))   # 2

    print("\nPart 2:")
    print("Case 1:", find_best_closing_time("Y Y N N"))       # 2
    print("Case 2:", find_best_closing_time("Y Y Y Y Y"))     # 5
    print("Case 3:", find_best_closing_time("N N N N N"))     # 0
    print("Case 4:", find_best_closing_time("N N Y Y"))       # 0
    print("Edge 1:", find_best_closing_time(""))              # 0
    print("Edge 2:", find_best_closing_time("Y"))             # 1
    print("Edge 3:", find_best_closing_time("N"))             # 0
    print("Edge 4:", find_best_closing_time("Y N Y"))         # 1

    print("\nPart 3:")
    log1 = "BEGIN Y Y N N END BEGIN Y Y Y Y Y END"
    print("Case 1:", get_best_closing_times(log1))  # [2, 5]

    log2 = "BEGIN N N N N N END"
    print("Case 2:", get_best_closing_times(log2))  # [0]

    log3 = "BEGIN N N Y Y END"
    print("Case 3:", get_best_closing_times(log3))  # [0]

    log4 = "BEGIN Y END BEGIN N END BEGIN Y N Y END"
    print("Case 4:", get_best_closing_times(log4))  # [1, 0, 1]

    log5 = "BEGIN BEGIN Y N Y END END"
    print("Edge 1:", get_best_closing_times(log5))  # []

    log6 = "BEGIN Y N Y"
    print("Edge 2:", get_best_closing_times(log6))  # []

    log7 = "FOO BEGIN Y N Y END BAR BEGIN N END"
    print("Edge 3:", get_best_closing_times(log7))  # [1, 0]

    # print("\nPart 4:")
    # base_dir = os.path.dirname(__file__)
    # filepath = os.path.join(base_dir, "myfile.txt")
    # print("Resolved path:", filepath)
    # print("File Test Case:", get_best_closing_times_v2(filepath))                