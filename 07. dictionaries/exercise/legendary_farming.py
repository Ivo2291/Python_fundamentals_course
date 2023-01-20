def legendary_item(some_item):
    item = ""
    if some_item == "shards":
        item = "Shadowmourne"
    elif some_item == "fragments":
        item = "Valanyr"
    elif some_item == "motes":
        item = "Dragonwrath"

    return item


items_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_items_dict = {}
materials_are_enough = False
leg_item = ""

while True:
    items = input().split()

    for value, material in zip(items[0::2], items[1::2]):
        quantity = int(value)
        current_material = material.lower()

        if current_material == "shards" or current_material == "fragments" or current_material == "motes":
            items_dict[current_material] += quantity

            if items_dict[current_material] >= 250:
                items_dict[current_material] -= 250
                materials_are_enough = True
                leg_item = legendary_item(current_material)
                break
        else:
            if current_material in junk_items_dict:
                junk_items_dict[current_material] += quantity
            else:
                junk_items_dict[current_material] = quantity

    if materials_are_enough:
        break

print(f"{leg_item} obtained!")

for key, value in items_dict.items():
    print(f"{key}: {value}")

for key, value in junk_items_dict.items():
    print(f"{key}: {value}")
