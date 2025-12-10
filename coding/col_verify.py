# Parse the csv string -> a list of rows(excl header)
def parse_csv(data: str) -> list[list[str]]:
    lines = data.strip().split("\n")
    return [line.split(",") for line in lines[1:]] # skip header

# rule 1: all non empty and valid
def rule_non_empty(row: list[str], exp_len: int) -> bool:
    return len(row) == exp_len and all(cell.strip() != "" for cell in row)

# rule 2: col5's length should be in [5, 31] (clean empty space)
def rule_col5_len(row: list[str]) -> bool:
    col5 = row[4].strip()
    return 5 <= len(col5) <= 31

# rule 3: col2 not incl forbidden words
def rule_col2_no_keywords(row: list[str], keywords: list[str]) -> bool:
    words_set = set(word.lower() for word in row[1].strip().split())
    keywords_set = set(k.lower() for k in keywords)
    return len(words_set & keywords_set) == 0

# rule 4: col2' words should have at least 50% appeart in col4 or col5
def rule_col2_word_match(row: list[str]) -> bool:
    c2, c4, c5 = row[1], row[3], row[4]
    
    def tokenize(s: str) -> set[str]:
        ignore = {"llc", "inc"}
        return set(
            word.lower()
            for word in s.strip().split()
            if word.strip() and word.lower() not in ignore
        )
    
    w2 = tokenize(c2)
    if not w2:
        return False
    w4 = tokenize(c4)
    w5 = tokenize(c5)

    def match_rate(target: set[str]) -> float:
        if not target:
            return 0.0
        return len(w2 & target) / len(w2)
    
    return match_rate(w4) >= 0.5 or match_rate(w5) >= 0.5

def validate_rows(data: str) -> list[str]:
    header = data.strip().split("\n")[0].split(",")
    exp_len = len(header)
    rows = parse_csv(data)
    res: list[str] = []

    forbidden = ["company", "firm", "co.", "corporation", "group"]

    for row in rows:
        c2_val = row[1] if len(row) > 1 else ""

        if not rule_non_empty(row, exp_len):
            res.append(f"NOT VERIFIED: {c2_val}")
            continue

        if not rule_col5_len(row):
            res.append(f"NOT VERIFIED: {c2_val}")
            continue

        if not rule_col2_no_keywords(row, forbidden):
            res.append(f"NOT VERIFIED: {c2_val}")
            continue

        if not rule_col2_word_match(row):
            res.append(f"NOT VERIFIED: {c2_val}")
            continue

        res.append(f"VERIFIED: {c2_val}")
    
    return res

# Test
if __name__ == "__main__":
    data = (
        "col1,col2,col3,col4,col5,col6\n"
        "a,land water,c,d,land water LLC,f\n"
        "a,Good Company,c,d,land water,f\n"
        "a,b,c,d,e,f\n"
        "1,2,3,,5,6"
    )

    print("Main sample:")
    for line in validate_rows(data):
        print(line)
    # exp：
    # VERIFIED: land water
    # NOT VERIFIED: Good Company
    # NOT VERIFIED: b
    # NOT VERIFIED: 2

    print("\nEdge 1:")
    data1 = "col1,col2,col3,col4,col5,col6\na,hello world,c,d,hello world LLC,f"
    print(validate_rows(data1))
    # Expected: ['VERIFIED: hello world']

    print("\nEdge 2:")
    data2 = "col1,col2,col3,col4,col5,col6\na,b,c,,e,f"
    print(validate_rows(data2))
    # Expected: ['NOT VERIFIED: b']

    print("\nEdge 3:")
    data3 = "col1,col2,col3,col4,col5,col6\na,b,c,d,x,f"
    print(validate_rows(data3))
    # Expected: ['NOT VERIFIED: b']

    print("\nEdge 4:")
    data4 = (
        "col1,col2,col3,col4,col5,col6\n"
        "a,b,c,d,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,f"
    )
    print(validate_rows(data4))
    # Expected: ['NOT VERIFIED: b']

    print("\nEdge 5:")
    data5 = "col1,col2,col3,col4,col5,col6\na,Best Company,c,d,Somewhere LLC,f"
    print(validate_rows(data5))
    # Expected: ['NOT VERIFIED: Best Company']

    print("\nEdge 6:")
    data6 = "col1,col2,col3,col4,col5,col6\na,sky blue ocean,c,d,green yellow pink,f"
    print(validate_rows(data6))
    # Expected: ['NOT VERIFIED: sky blue ocean']

    print("\nEdge 7:")
    data7 = "col1,col2,col3,col4,col5,col6\na,apple banana,c,d,banana orange,f"
    print(validate_rows(data7))
    # Expected: ['VERIFIED: apple banana']

    print("\nEdge 8:")
    data8 = "col1,col2,col3,col4,col5,col6\na,Companyish Name,c,d,Companyish land,f"
    print(validate_rows(data8))
    # Expected: ['VERIFIED: Companyish Name']

    print("\nEdge 9:")
    data9 = "col1,col2,col3,col4,col5,col6\na,LLC Inc,c,d,something real,f"
    print(validate_rows(data9))
    # Expected: ['NOT VERIFIED: LLC Inc']

    print("\nEdge 10:")
    data10 = "col1,col2,col3,col4,col5,col6\na,land water stone,c,d,land water LLC,f"
    print(validate_rows(data10))
    # Expected: ['VERIFIED: land water stone']