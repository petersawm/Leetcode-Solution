# Part 1: 
def kyc_verify_p1(records):
    req = [
        "business_name",
        "business_profile_name",
        "full_statement_descriptor",
        "short_statement_descriptor",
        "url",
        "product_description",
    ]

    # part 3: blocklist
    blocklist = {
        "ONLINE STORE",
        "ECOMMERCE",
        "RETAIL",
        "SHOP",
        "GENERAL MERCHANDISE",
    }

    res = []
    for rec in records:
        name = rec.get("business_name", "").strip()
        ok = True
        for f in req:
            v = rec.get(f, "")
            if v is None or str(v).strip() == "":
                ok = False
                break
        # Part 2: check length
        if ok:
            fsd = str(rec.get("full_statement_descriptor", "")).strip()
            if not (5 <= len(fsd) <= 31):
                ok = False

        # Part 3
        if ok:
            norm = str(rec.get("full_statement_descriptor", "")).strip().upper()
            if norm in blocklist:
                ok = False

        if ok:
            res.append(f"VERIFIED: {name}")
        else:
            res.append(f"NOT VERIFIED: {name}")
    return res

# Test
if __name__ == "__main__":
    part1_input = [
        {
            "business_name": "Pawsome Pets Inc.",
            "business_profile_name": "Pawsome Pets",
            "full_statement_descriptor": "PAWSOME PETS",
            "short_statement_descriptor": "PAWSOME",
            "url": "https://pawsome.example",
            "product_description": "Pet accessories",
        },
        {
            "business_name": "Bean Bliss Coffee Company",
            "business_profile_name": "Bean Bliss",
            "full_statement_descriptor": "  ", 
            "short_statement_descriptor": "BEAN",
            "url": "https://beanbliss.example",
            "product_description": "Coffee & snacks",
        },
    ]
    print("=== Part 1 ===")
    for line in kyc_verify_p1(part1_input):
        print(line)

    # VERIFIED: Pawsome Pets Inc.
    # NOT VERIFIED: Bean Bliss Coffee Company

    part2_input = [
        {
            "business_name": "Oakridge Furniture Crafters LLC",
            "business_profile_name": "Oakridge Furniture",
            "full_statement_descriptor": "OAKRIDGE CUSTOM WOODWORKING AND FURNITURE EMPORIUM",  
            "short_statement_descriptor": "OAK",
            "url": "https://oakridge.example",
            "product_description": "Custom furniture",
        },
        {
            "business_name": "Information Technology Consulting Solutions Inc.",
            "business_profile_name": "ITCS",
            "full_statement_descriptor": "ITCS", 
            "short_statement_descriptor": "ITCS",
            "url": "https://itcs.example",
            "product_description": "Consulting",
        },
        {
            "business_name": "Om Yoga and Wellness Center",
            "business_profile_name": "Om Yoga",
            "full_statement_descriptor": "OM YOGA",  
            "short_statement_descriptor": "OM",
            "url": "https://omyoga.example",
            "product_description": "Yoga studio",
        },
    ]
    print("\n=== Part 2 ===")
    for line in kyc_verify_p1(part2_input):
        print(line)
    # NOT VERIFIED: Oakridge Furniture Crafters LLC
    # NOT VERIFIED: Information Technology Consulting Solutions Inc.
    # VERIFIED: Om Yoga and Wellness Center

    part3_input = [
        {
            "business_name": "Pawsome Pets Inc.",
            "business_profile_name": "Pawsome Pets",
            "full_statement_descriptor": "PAWSOME PETS",
            "short_statement_descriptor": "PAWSOME",
            "url": "https://pawsome.example",
            "product_description": "Pet accessories",
        },
        {
            "business_name": "Bean Bliss Coffee Company",
            "business_profile_name": "Bean Bliss",
            "full_statement_descriptor": "  ",  
            "short_statement_descriptor": "BEAN",
            "url": "https://beanbliss.example",
            "product_description": "Coffee & snacks",
        },
        {
            "business_name": "Oakridge Furniture Crafters LLC",
            "business_profile_name": "Oakridge Furniture",
            "full_statement_descriptor": "OAKRIDGE CUSTOM WOODWORKING AND FURNITURE EMPORIUM",
            "short_statement_descriptor": "OAK",
            "url": "https://oakridge.example",
            "product_description": "Custom furniture",
        },
        {
            "business_name": "Om Yoga and Wellness Center",
            "business_profile_name": "Om Yoga",
            "full_statement_descriptor": "OM YOGA",
            "short_statement_descriptor": "OM",
            "url": "https://omyoga.example",
            "product_description": "Yoga studio",
        },
        {
            "business_name": "Information Technology Consulting Solutions Inc.",
            "business_profile_name": "ITCS",
            "full_statement_descriptor": "ITCS",
            "short_statement_descriptor": "ITCS",
            "url": "https://itcs.example",
            "product_description": "Consulting",
        },
        # Part3 失败示例：黑名单（大小写无关）
        {
            "business_name": "Global Goods Marketplace Inc.",
            "business_profile_name": "Global Goods",
            "full_statement_descriptor": "Retail",  # 命中黑名单 RETAIL
            "short_statement_descriptor": "GG",
            "url": "https://globalgoods.example",
            "product_description": "Marketplace",
        },
        # 通过的
        {
            "business_name": "Evergreen Digital Strategies LLC",
            "business_profile_name": "Evergreen Digital",
            "full_statement_descriptor": "EVERGREEN DIGITAL",
            "short_statement_descriptor": "EG",
            "url": "https://evergreen.example",
            "product_description": "Digital consulting",
        },
        # 通过的
        {
            "business_name": "Sweet Dreams Creamery LLC",
            "business_profile_name": "Sweet Dreams",
            "full_statement_descriptor": "SWEET DREAMS",
            "short_statement_descriptor": "SD",
            "url": "https://sweetdreams.example",
            "product_description": "Ice cream shop",
        },
        # Part3 失败示例：黑名单 ONLINE STORE
        {
            "business_name": "Global Financial Advisory Services Inc.",
            "business_profile_name": "GFAS",
            "full_statement_descriptor": "Online Store",
            "short_statement_descriptor": "GFAS",
            "url": "https://gfas.example",
            "product_description": "Advisory",
        },
        # Part3 失败示例：黑名单 GENERAL MERCHANDISE
        {
            "business_name": "Northwest Innovation Technologies Corporation",
            "business_profile_name": "Northwest Innovation",
            "full_statement_descriptor": "GENERAL MERCHANDISE",
            "short_statement_descriptor": "NWIT",
            "url": "https://nwit.example",
            "product_description": "Tech solutions",
        },
    ]
    print("\n=== Part 3 ===")
    for line in kyc_verify_p1(part3_input):
        print(line)

    # VERIFIED: Pawsome Pets Inc.
    # NOT VERIFIED: Bean Bliss Coffee Company
    # NOT VERIFIED: Oakridge Furniture Crafters LLC
    # VERIFIED: Om Yoga and Wellness Center
    # NOT VERIFIED: Information Technology Consulting Solutions Inc.
    # NOT VERIFIED: Global Goods Marketplace Inc.
    # VERIFIED: Evergreen Digital Strategies LLC
    # VERIFIED: Sweet Dreams Creamery LLC
    # NOT VERIFIED: Global Financial Advisory Services Inc.
    # NOT VERIFIED: Northwest Innovation Technologies Corporation