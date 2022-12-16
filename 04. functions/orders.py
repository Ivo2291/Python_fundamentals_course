def calculate_prices(some_product, some_quantity):
    if some_product == "coffee":
        return some_quantity * 1.5
    elif some_product == "coke":
        return some_quantity * 1.4
    elif some_product == "water":
        return some_quantity * 1
    elif some_product == "snacks":
        return some_quantity * 2


product = input()
quantity = int(input())
total_price = calculate_prices(product, quantity)

print(f"{total_price:.2f}")
