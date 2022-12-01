lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_counter = 0

for day in range(1, lost_fights_count + 1):

    if day % 2 == 0:
        expenses += helmet_price
    if day % 3 == 0:
        expenses += sword_price

        if day % 2 == 0:
            expenses += shield_price
            shield_counter += 1

            if shield_counter == 2:
                expenses += armor_price
                shield_counter = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
