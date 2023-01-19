input_text = input()
bakery = {}

while input_text != "statistics":
    split_input = input_text.split(": ")
    product = split_input[0]
    quantity = int(split_input[1])

    if product in bakery:
        bakery[product] += quantity
    else:
        bakery[product] = quantity

    input_text = input()

total_products = len(bakery)
total_quantity = sum(bakery.values())

print("Products in stock:")

for item in bakery:
    print(f"- {item}: {bakery[item]}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
