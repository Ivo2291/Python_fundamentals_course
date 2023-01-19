info_list = input().split()
bakery_dict = {}

for product in range(0, len(info_list), 2):
    food = info_list[product]
    quantity = info_list[product + 1]

    bakery_dict[food] = int(quantity)

print(bakery_dict)
