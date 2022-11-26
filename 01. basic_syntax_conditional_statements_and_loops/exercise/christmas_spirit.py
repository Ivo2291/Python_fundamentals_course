quantity = int(input())
days = int(input())

christmas_spirit = 0
total_costs = 0
condition_5th_day = False

for day in range(1, days + 1):
    condition_5th_day = False

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_costs += 2 * quantity
        christmas_spirit += 5

    if day % 3 == 0:
        total_costs += (5 * quantity) + (3 * quantity)
        christmas_spirit += 13
        condition_5th_day = True

    if day % 5 == 0:
        total_costs += 15 * quantity
        christmas_spirit += 17

        if condition_5th_day:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_costs += 23

        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {christmas_spirit}")

# second_solution

quantity = int(input())
days = int(input())
total_cost = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_cost += quantity * ornament_set_price
        total_spirit += 5

    if current_day % 3 == 0:
        total_cost += quantity * (tree_skirt_price + tree_garlands_price)
        total_spirit += 13

    if current_day % 5 == 0:
        total_cost += quantity * tree_lights_price
        total_spirit += 17

        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garlands_price + tree_lights_price

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
