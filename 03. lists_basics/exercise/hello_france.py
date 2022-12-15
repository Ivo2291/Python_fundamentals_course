items = input().split("|")
budget = float(input())

new_prices_of_items = []
final_prices = []
profit = 0
price_is_good = False

for item in items:
    current_item = item.split("->")
    item_type = current_item[0]
    price = float(current_item[1])
    price_is_good = False

    if item_type == "Clothes":
        if price <= 50:
            price_is_good = True

    elif item_type == "Shoes":
        if price <= 35:
            price_is_good = True

    elif item_type == "Accessories":
        if price <= 20.5:
            price_is_good = True

    if price_is_good:
        if budget >= price:
            budget -= price
            profit += price * 0.4
            new_price = price + (price * 0.4)
            final_prices.append(new_price)
            new_prices_of_items.append(f"{new_price:.2f}")

print(" ".join(new_prices_of_items))
print(f"Profit: {profit:.2f}")

total_money_left = budget + sum(final_prices)

if total_money_left >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
