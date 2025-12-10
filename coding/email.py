# Part 1: only users and three email(welcome, upcoming exp, exp)
def parse_users(user_requests):
    users_data = []
    for req in user_requests:
        name = req["name"]
        plan = req["plan"]
        begin = req["begin_date"]
        dur = req["duration"]
        users_data.append(
            {
                "name": name,
                "plan": plan,
                "begin_date": begin,
                "duration": dur,
            }
        )
    
    # sort by begin date
    users_data.sort(key=lambda x: x["begin_date"])
    return users_data

def create_email_events(users_data):
    events = []
    for u in users_data:
        name = u["name"]
        plan = u["plan"]
        begin = u["begin_date"]
        dur = u["duration"]

        # welcome
        events.append(
            {
                "time": begin,
                "name": name,
                "plan": plan,
                "type": "Welcome",
            }
        )

        # upcoming exp(15 days, need to clarify)
        up_time = begin + dur - 15
        events.append(
            {
                "time": up_time,
                "name": name,
                "plan": plan,
                "type": "Upcoming expiration"
            }
        )

        # expired
        exp_time = begin + dur
        events.append(
            {
                "time": exp_time,
                "name": name,
                "plan": plan,
                "type": "Expired"
            }
        )
    
    # sort by time
    events.sort(key=lambda x: x["time"])
    return events

def send_emails(user_requests):
    users_data = parse_users(user_requests)
    events = create_email_events(users_data)

    for e in events:
        print(
            f"{e['time']}: [{e['type']}] {e['name']}, subscribe in plan {e['plan']}"
        )

# Part 2: add plan change
def create_email_events_with_changes(users_data, changes):
    events = create_email_events(users_data)

    changes_sorted = sorted(changes, key=lambda c: c["change_date"])

    # name -> cur plan(for multi changes)
    plan_map = {u["name"]:  u["plan"] for u in users_data}

    for c in changes_sorted:
        name = c["name"]
        new_plan = c["new_plan"]
        t = c["change_date"]

        events.append(
            {
                "time": t,
                "name": name,
                "plan": new_plan,
                "type": "Changed",
            }
        )

        # update all after 
        plan_map[name] = new_plan
        for e in events:
            if e["time"] < t:
                continue
            if e["name"] == name:
                e["plan"] = new_plan
    
    events.sort(key=lambda x:x["time"])
    return events

def send_emails_with_changes(user_requests, change_requests):
    users_data = parse_users(user_requests)
    events = create_email_events_with_changes(users_data, change_requests)

    for e in events:
        print(
            f"{e['time']}: [{e['type']}] {e['name']}, subscribe in plan {e['plan']}"
        )

# Part 3: add extension(renewed)
# extension change_date send an email[Renewed]
# exp date + extension + new upcoming exp

def create_email_events_with_changes_ext(users_data, changes):
    # get the basic events
    events = create_email_events(users_data)

    # name -> cur plan/ cur exp date
    plan_map = {u["name"]: u["plan"] for u in users_data}
    exp_map = {u["name"]: u["begin_date"] + u["duration"] for u in users_data}
    UP_OFFSET = 15

    changes_sorted = sorted(changes, key=lambda c: c["change_date"])

    for c in changes_sorted:
        name = c["name"]
        t = c["change_date"]

        # plan change
        if "new_plan" in c:
            new_plan = c["new_plan"]
            events.append(
                {
                    "time": t,
                    "name": name,
                    "plan": new_plan,
                    "type": "Changed",
                }
            )
            plan_map[name] = new_plan

            for e in events:
                if e["time"] < t:
                    continue
                if e["name"] == name:
                    e["plan"] = new_plan
        
        # extension
        elif "extension" in c:
            ext = c["extension"]
            cur_plan = plan_map.get(name, None)
            if cur_plan is None:
                continue

            # Renewed event
            events.append(
                {
                    "time": t,
                    "name": name,
                    "plan": cur_plan,
                    "type": "Renewed",
                }
            )

            # update ola exp date
            old_exp = exp_map[name]
            new_exp = old_exp + ext
            exp_map[name] = new_exp

            # find the later expired events, modify to new_exp
            for e in events:
                if e["name"] == name and e["type"] == "Expired" and e["time"] >= t:
                    e["time"] = new_exp
            
            events.append(
                {
                    "time": new_exp - UP_OFFSET,
                    "name": name,
                    "plan": cur_plan,
                    "type": "Upcoming expiration",
                }
            )
    events.sort(key=lambda x: x["time"])
    return events

def send_emails_with_changes_ext(user_requests, change_requests):
    users_data = parse_users(user_requests)
    events = create_email_events_with_changes_ext(users_data, change_requests)
    
    for e in events:
        print(
            f"{e['time']}: [{e['type']}] {e['name']}, subscribe in plan {e['plan']}"
        )

# Part 4: each user has their notification offset
def parse_users_expiry(user_requests):
    users_data = []
    for req in user_requests:
        name = req["name"]
        plan = req["plan"]
        begin = req["begin_date"]
        dur = req["duration"]
        exp_offset = req["expiry"]

        users_data.append(
            {
                "name": name,
                "plan": plan,
                "begin_date": begin,
                "duration": dur,
                "expiry": exp_offset,
            }
        )
    
    users_data.sort(key=lambda x: x["begin_date"])
    return users_data

def create_email_events_with_changes_ext_expiry(users_data, changes):
    events = []
    plan_map = {}
    exp_map = {}
    offset_map = {}

    for u in users_data:
        name = u["name"]
        plan = u["plan"]
        begin = u["begin_date"]
        dur = u["duration"]
        off = u["expiry"]

        plan_map[name] = plan
        exp = begin + dur
        exp_map[name] = exp
        offset_map[name] = off

        # Welcome
        events.append(
            {
                "time": begin,
                "name": name,
                "plan": plan,
                "type": "Welcome",
            }
        )

        # Upcoming exp
        up_time = exp - off
        if up_time >= begin:
            events.append(
                {
                    "time": up_time,
                    "name": name,
                    "plan": plan,
                    "type": "Upcoming expiration",
                }
            )
        
        # Expired
        events.append(
            {
                "time": exp,
                "name": name,
                "plan": plan,
                "type": "Expired",
            }
        )
    
    # handle changes
    changes_sorted = sorted(changes, key=lambda c: c["change_date"])

    for c in changes_sorted:
        name = c["name"]
        t = c["change_date"]

        # plan change
        if "new_plan" in c:
            new_plan = c["new_plan"]
            events.append(
                {
                    "time": t,
                    "name": name,
                    "plan": new_plan,
                    "type": "Changed",
                }
            )
            
            plan_map[name] = new_plan

            for e in events:
                if e["time"] < t:
                    continue
                if e["name"] == name:
                    e["plan"] = new_plan
        
        # extension
        elif "extension" in c:
            ext = c["extension"]
            cur_plan = plan_map.get(name, None)
            if cur_plan is None:
                continue
            events.append(
                {
                    "time": t,
                    "name": name,
                    "plan": cur_plan,
                    "type": "Renewed",
                }
            )

            old_exp = exp_map[name]
            new_exp = old_exp + ext
            exp_map[name] = new_exp
            off = offset_map[name]

            # update later expired
            for e in events:
                if e["name"] == name and e["type"] == "Expired" and e["time"] >= t:
                    e["time"] = new_exp
            
            # new upcoming(old keep)
            up_time = new_exp - off
            events.append(
                {
                    "time": up_time,
                    "name": name,
                    "plan": cur_plan,
                    "type": "Upcoming expiration",
                }
            )
    
    events.sort(key=lambda x: x["time"])
    return events

def send_emails_with_changes_ext_expiry(user_requests, change_requests):
    users_data = parse_users_expiry(user_requests)
    events = create_email_events_with_changes_ext_expiry(users_data, change_requests)
    
    for e in events:
        print(
            f"{e['time']}: [{e['type']}] {e['name']}, subscribe in plan {e['plan']}"
        )

# Test

if __name__ == "__main__":
    # ---------- Part 1 ----------
    print("*************** Part 1 ***************")
    users = [
        {"name": "A", "plan": "X", "begin_date": 0, "duration": 30},
        {"name": "B", "plan": "Y", "begin_date": 1, "duration": 15},
    ]
    send_emails(users)
    # expected:
    # 0: [Welcome] A ...
    # 1: [Welcome] B ...
    # 1: [Upcoming expiration] B ...
    # 15: [Upcoming expiration] A ...
    # 16: [Expired] B ...
    # 30: [Expired] A ...

    # ---------- Part 2 ----------
    print("\n*************** Part 2 ***************")
    changes = [
        {"name": "A", "new_plan": "Y", "change_date": 5},
    ]
    send_emails_with_changes(users, changes)

    # ---------- Part 3 ----------
    print("\n*************** Part 3 ***************")
    changes = [
        {"name": "A", "new_plan": "Y", "change_date": 5},
        {"name": "B", "extension": 15, "change_date": 3},
    ]
    send_emails_with_changes_ext(users, changes)

    print("\n*************** Part 3 (multi change) ***************")
    users2 = [
        {"name": "C", "plan": "P1", "begin_date": 0, "duration": 20},
    ]
    changes2 = [
        {"name": "C", "new_plan": "P2", "change_date": 5},
        {"name": "C", "extension": 10, "change_date": 8},
        {"name": "C", "new_plan": "P3", "change_date": 15},
    ]
    send_emails_with_changes_ext(users2, changes2)

    # ---------- Part 4 ----------
    print("\n*************** Part 4 ***************")
    users = [
        {
            "name": "A",
            "plan": "X",
            "begin_date": 0,
            "duration": 30,
            "expiry": 7,  
        },
        {
            "name": "B",
            "plan": "Y",
            "begin_date": 1,
            "duration": 10,
            "expiry": 3, 
        },
        {
            "name": "C",
            "plan": "Z",
            "begin_date": 2,
            "duration": 5,
            "expiry": 10,  # out of date -> do not send upcoming
        },
    ]
    changes = [
        {"name": "A", "new_plan": "Y", "change_date": 5},
        {"name": "B", "extension": 15, "change_date": 3},
    ]
    send_emails_with_changes_ext_expiry(users, changes)