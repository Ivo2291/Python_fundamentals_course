food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
pig_weight = float(input())

food_grams = food_quantity * 1000
hay_grams = hay_quantity * 1000
cover_grams = cover_quantity * 1000
weight_in_grams = pig_weight * 1000
food_is_enough = True

for day in range(1, 31):
    if food_grams <= 300:
        food_is_enough = False
        break

    else:
        food_grams -= 300
        hay_per_day = food_grams * 0.05
        cover_per_day = weight_in_grams / 3

    if hay_grams < hay_per_day or cover_grams < cover_per_day:
        food_is_enough = False
        break

    else:
        if day % 2 == 0:
            hay_grams -= hay_per_day
        if day % 3 == 0:
            cover_grams -= cover_per_day

if food_is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {(food_grams / 1000):.2f},"
          f" Hay: {(hay_grams / 1000):.2f}, Cover: {(cover_grams / 1000):.2f}.")

else:
    print("Merry must go to the pet store!")
