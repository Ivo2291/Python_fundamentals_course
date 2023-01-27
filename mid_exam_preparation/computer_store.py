command = input()
price_with_taxes = 0
price_without_taxes = 0
amount_of_taxes = 0
order_is_valid = True

while command != "special" and command != "regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")

    else:
        current_tax = price * 0.2
        amount_of_taxes += current_tax
        price_without_taxes += price
        price_with_taxes += price + current_tax

    command = input()

if command == "special":
    price_with_taxes -= price_with_taxes * 0.1

if price_with_taxes == 0:
    order_is_valid = False

if order_is_valid:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")

else:
    print("Invalid order!")
