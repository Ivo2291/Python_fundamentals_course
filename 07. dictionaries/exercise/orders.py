command = input()
products_data = {}

while command != "buy":

    split_command = command.split()

    product = split_command[0]
    price = float(split_command[1])
    quantity = int(split_command[2])

    if product not in products_data:
        products_data[product] = [price, quantity]
    else:
        products_data[product][1] += quantity

    products_data[product][0] = price

    command = input()

for key, value in products_data.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
