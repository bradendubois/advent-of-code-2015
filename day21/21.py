from sys import stdin
from itertools import product

l = [x.split(" ") for x in stdin.read().split("\n")]

boss_hit_points = int(l[0][2])
boss_damage = int(l[1][1])
boss_armor = int(l[2][1])

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armor = [
    (0, 0, 0),  # No Armor
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [
    (0, 0, 0),  # No Ring
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

cost = lambda x: sum(y[0] for y in x)

equipment_combos = set(product(weapons, armor, rings, rings))

# Filter out the ones where a ring was selected twice
# equipment_combos -= {x for x in equipment_combos if x[2] != (0, 0, 0) and x[2] == x[3]}


price_ascending = sorted(equipment_combos, key=cost)


def winnable(equipment):

    def game(damage, armor):
        
        player_health = 100
        enemy_health = boss_hit_points

        while player_health > 0:
            enemy_health -= max(1, damage - boss_armor)
            if enemy_health <= 0:
                return True

            player_health -= max(1, boss_damage - armor)

        return False


    damage = sum(x[1] for x in equipment)
    armor = sum(x[2] for x in equipment)

    return game(damage, armor)



# Part One
for gear in price_ascending:
    if winnable(gear):
        print(cost(gear))
        break


# Part Two
price_descending = price_ascending[::-1]
for gear in price_descending:
    if not winnable(gear):
        print(cost(gear))
        break
