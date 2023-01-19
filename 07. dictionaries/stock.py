info_list = input().split()
searched_products = input().split()
bakery_dict = {}

for product in range(0, len(info_list), 2):
    food = info_list[product]
    quantity = info_list[product + 1]
    bakery_dict[food] = int(quantity)

for item in searched_products:

    if item in bakery_dict:
        print(f"We have {bakery_dict[item]} of {item} left")

    else:
        print(f"Sorry, we don't have {item}")
