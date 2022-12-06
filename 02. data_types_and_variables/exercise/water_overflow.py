number = int(input())

capacity = 255
litters_in_tank = 0

for num in range(number):
    liters_of_water = int(input())

    if liters_of_water > capacity:
        print("Insufficient capacity!")
        continue

    capacity -= liters_of_water
    litters_in_tank += liters_of_water

print(litters_in_tank)
