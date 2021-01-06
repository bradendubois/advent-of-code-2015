boss_hit_points = 55
boss_damage = 8

def options(state):

    mana_left = state["mana"]

    options = set()

    if mana_left >= 53:
        options.add("missile")

    if mana_left >= 73:
        options.add("drain")

    if state["shield_turns"] == 0 and mana_left >= 113:
        options.add("shield")

    if state["poison_turns"] == 0 and mana_left >= 173:
        options.add("poison")

    if state["recharge_turns"] == 0 and mana_left >= 229:
        options.add("recharge")

    return options


def game(hard=False):

    initial = {
        "player_hp": 50,
        "mana": 500,
        "boss_hp": boss_hit_points,
        "shield_turns": 0,
        "poison_turns": 0,
        "recharge_turns": 0,
        "mana_spent": 0,
        "p1_turn": True
    }

    queue = [initial]
    lowest = None

    while len(queue):

        c = queue.pop(0)
        if lowest and c["mana_spent"] > lowest:
            continue

        if c["poison_turns"] > 0:
            c["boss_hp"] -= 3
        
        if c["recharge_turns"] > 0:
            c["mana"] += 101
        
        c["shield_turns"] = max(c["shield_turns"] - 1, 0)
        c["poison_turns"] = max(c["poison_turns"] - 1, 0)
        c["recharge_turns"] = max(c["recharge_turns"] - 1, 0)

        if c["boss_hp"] <= 0:
            spent = c["mana_spent"]
            if lowest is None or spent < lowest:
                lowest = spent
            continue

        if c["p1_turn"]:

            if hard:
                c["player_hp"] -= 1

            o = options(c)
            if len(o) == 0 or c["player_hp"] <= 0:
                continue

            for option in o:
                
                n = c.copy()

                if option == "missile":
                    n["mana"] -= 53
                    n["mana_spent"] += 53
                    n["boss_hp"] -= 4    

                elif option == "drain":
                    n["mana"] -= 73
                    n["mana_spent"] += 73
                    n["boss_hp"] -= 2
                    n["player_hp"] += 2

                elif option == "shield":
                    n["mana"] -= 113
                    n["mana_spent"] += 113
                    n["shield_turns"] = 6
                
                elif option == "poison":
                    n["mana"] -= 173
                    n["mana_spent"] += 173
                    n["poison_turns"] = 6

                elif option == "recharge":
                    n["mana"] -= 229
                    n["mana_spent"] += 229
                    n["recharge_turns"] = 5

                if n["boss_hp"] <= 0:
                    spent = n["mana_spent"]
                    if lowest is None or spent < lowest:
                        lowest = spent
                    continue

                n["p1_turn"] = False
                queue.append(n)

        else:
            armor = 7 if c["shield_turns"] > 0 else 0
            damage = max(boss_damage - armor, 1)
            c["player_hp"] -= damage

            if c["player_hp"] <= 0:
                continue

            c["p1_turn"] = True
            queue.append(c)

    return lowest

# Part One
print(game())

# Part Two
print(game(True))
