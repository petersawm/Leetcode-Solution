# DRY: shared helpers
def _validate_inputs(header: str, supported_languages):
    if not header or not header.strip():
        return "header is not valid"
    if not supported_languages:
        return "supported_languages is not valid"
    return None # ok

def _split_header_list(header: str):
    return [item.strip() for item in header.split(",") if item.strip()]

def _supported_views(supported_languages):
    sup_list = list(supported_languages)
    sup_set = set(supported_languages) # filter duplicate
    return sup_list, sup_set

# Part 1: exact match only
def parse_accept_language(header, supported_languages):
    err = _validate_inputs(header, supported_languages)
    if err:
        return err
    
    pref_list = _split_header_list(header)
    _, sup_set = _supported_views(supported_languages)

    res = [tag for tag in pref_list if tag in sup_set]
    return res

# Part 2: add generic tags like "fr"
def parse_accept_language_v2(header, supported_languages):
    err = _validate_inputs(header, supported_languages)
    if err:
        return err
    
    pref_list = _split_header_list(header)
    sup_list, sup_set = _supported_views(supported_languages)

    res = []
    seen = set()

    for tag in pref_list:
        # exact match
        if tag in sup_set and tag not in seen:
            res.append(tag)
            seen.add(tag)
            continue
        # generic match, eg "fr" -> "fr-CA", "fr-FR"
        if "-" not in tag and tag != "*":
            prefix = tag + "-"
            for s in sup_list:
                if s.startswith(prefix) and s not in seen:
                    res.append(s)
                    seen.add(s)
    return res

# Part 3: extend with wildcard
def parse_accept_language_ordered(header, supported_languages):
    err = _validate_inputs(header, supported_languages)
    if err:
        return err
    
    pref_list = _split_header_list(header)
    sup_list, sup_set = _supported_views(supported_languages)

    res = []
    seen = set()

    for tag in pref_list:
        if tag == "*":
            # add all remaining supported languages
            for s in sup_list:
                if s not in seen:
                    res.append(s)
                    seen.add(s)
        elif tag in sup_set:
            # exact match
            if tag not in seen:
                res.append(tag)
                seen.add(tag)
        else:
            # generic
            if "-" not in tag:
                prefix = tag + "-"
                for s in sup_list:
                    if s.startswith(prefix) and s not in seen:
                        res.append(s)
                        seen.add(s)
    return res

# Part 4: add q-factors
def parse_accept_language_qfactor(header, supported_languages):
    err = _validate_inputs(header, supported_languages)
    if err:
        return err
    sup_list, _ = _supported_views(supported_languages)

    # parse header to (tag, q, index)
    entries = []
    for idx, raw in enumerate(_split_header_list(header)):
        parts = [p.strip() for p in raw.split(";")]
        tag = parts[0]
        q = 1.0
        if len(parts) >= 2 and parts[1].startswith("q="):
            try:
                q = float(parts[1][2:])
            except ValueError:
                q = 1.0 # default
        entries.append((tag, q, idx))
    
    def _match_spec(entry_tag, sup_tag):
        if entry_tag == "*":
            return 0
        if entry_tag == sup_tag:
            return 2
        if "-" not in entry_tag and sup_tag.startswith(entry_tag + "-"):
            return 1
        return None
    
    best = {} # best[lang] = (q, spec, entry_idx)
    for entry_tag, q, idx in entries:
        for s in sup_list:
            spec = _match_spec(entry_tag, s)
            if spec is None:
                continue
            if s not in best:
                best[s] = (q, spec, idx)
            else:
                cur_q, cur_spec, _ = best[s]
                if spec > cur_spec or (spec == cur_spec and q > cur_q): 
                    best[s] = (q, spec, idx)
    
    # only keep match supported
    items = []
    for sup_idx, s in enumerate(sup_list):
        if s in best:
            q, spec, idx = best[s]
            items.append((s, q, spec, idx, sup_idx))
    # q dest, spec dest, entry idx asc, sup idx asc
    items.sort(key=lambda x: (-x[1], -x[2], x[3], x[4]))
    return [s for (s, _, _, _, _) in items]

# Test
if __name__ == "__main__":
    print("part 1")
    print(parse_accept_language("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]))
    # Expected (by current code): ['en-US', 'fr-FR']
    print(parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]))
    # Expected: ['fr-FR']
    print(parse_accept_language("en-US", ["en-US", "fr-CA"]))
    # Expected: ['en-US']
    print(parse_accept_language("fr-CA, de-DE", ["en-US"]))
    # Expected: [] No match
    print(parse_accept_language(" en-US , fr-CA ", ["en-US", "fr-CA"]))
    # Expected: ['en-US', 'fr-CA']
    print(parse_accept_language("", ["en-US", "fr-CA"]))
    # Expected: "header is not valid"
    print(parse_accept_language("en-US, fr-CA", []))
    # Expected: "supported_languages is not valid"

    print("\npart 2")
    print(parse_accept_language_v2("en", ["en-US", "fr-CA", "fr-FR"]))
    # Expected: ['en-US']
    print(parse_accept_language_v2("fr", ["en-US", "fr-CA", "fr-FR"]))
    # Expected: ['fr-CA', 'fr-FR']
    print(parse_accept_language_v2("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"]))
    # Expected: ['fr-FR', 'fr-CA']
    print(parse_accept_language_v2("en-GB, en", ["en-US", "en-GB", "fr-FR"]))
    # Expected: ['en-GB', 'en-US']
    print(parse_accept_language_v2("en, en-US", ["en-US", "en-GB"]))
    # Expected: ['en-US', 'en-GB']
    print(parse_accept_language_v2("de", ["en-US", "fr-CA"]))
    # Expected: []
    print(parse_accept_language_v2("", ["en-US"]))
    # Expected: "header is not valid"

    print("\npart 3")
    print(parse_accept_language_ordered("en-US, *", ["en-US", "fr-CA", "fr-FR"]))
    # Expected: ['en-US', 'fr-CA', 'fr-FR'] keep supported order
    print(parse_accept_language_ordered("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"]))
    # Expected: ['fr-FR', 'fr-CA', 'en-US']
    print(parse_accept_language_ordered("*, en-US", ["en-US", "fr-FR"]))
    # Expected: ['en-US', 'fr-FR']
    print(parse_accept_language_ordered("fr, fr-FR", ["fr-FR", "fr-BR", "fr-CA"]))
    # Expected: ['fr-FR', 'fr-BR', 'fr-CA']
    print(parse_accept_language_ordered("fr-FR, fr", ["fr-FR", "fr-BR", "fr-CA"]))
    # Expected: ['fr-FR', 'fr-BR', 'fr-CA']
    print(parse_accept_language_ordered("*", ["en-US", "fr-FR"]))
    # Expected: ['en-US', 'fr-FR']
    print(parse_accept_language_ordered("en-US, *", ["en-US", "en-GB", "fr-FR"]))
    # Expected: ['en-US', 'en-GB', 'fr-FR']
    print(parse_accept_language_ordered("", ["en-US"]))
    # Expected: "header is not valid"
    print(parse_accept_language_ordered("en-US, fr", []))
    # Expected: "supported_languages is not valid"

    print("\npart 4 (q-factors)")
    print(
        parse_accept_language_qfactor(
            "fr-FR;q=1, fr-CA;q=0, fr;q=0.5",
            ["fr-FR", "fr-CA", "fr-BG"],
        )
    )
    # Expected (by current code): ['fr-FR', 'fr-BG', 'fr-CA']
    print(
        parse_accept_language_qfactor(
            "fr-FR;q=1, fr-CA;q=0, *;q=0.5",
            ["fr-FR", "fr-CA", "fr-BG", "en-US"],
        )
    )
    # Expected: ['fr-FR', 'fr-BG', 'en-US', 'fr-CA']
    print(
        parse_accept_language_qfactor(
            "fr-FR;q=1, fr-CA;q=0.8, *;q=0.5",
            ["fr-FR", "fr-CA", "fr-BG", "en-US"],
        )
    )
    # Expected: ['fr-FR', 'fr-CA', 'fr-BG', 'en-US']
    print(parse_accept_language_qfactor("fr-FR, fr", ["fr-FR", "fr-BR", "fr-CA"]))
    # Expected: ['fr-FR', 'fr-BR', 'fr-CA']
    print(parse_accept_language_qfactor("*, fr;q=0.5", ["fr-FR", "en-US"]))
    # Expected (by current code): ['en-US', 'fr-FR']
    print(parse_accept_language_qfactor("en-US;q=0", ["en-US", "fr-FR"]))
    # Expected (by current code): ['en-US']
    print(parse_accept_language_qfactor("fr-FR;q=xyz, fr", ["fr-FR", "fr-CA"]))
    # Expected: ['fr-FR', 'fr-CA']
    print(parse_accept_language_qfactor("fr-CA;q=0, *;q=0.5", ["fr-CA", "fr-FR"]))
    # Expected (by current code): ['fr-FR', 'fr-CA']