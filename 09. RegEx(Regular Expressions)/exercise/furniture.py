import re

command = input()
total_cost = 0
furniture_bought = []
pattern = r">>(?P<furniture>[A-za-z]+)<<(?P<price>[0-9]+[\.0-9]*)!(?P<quantity>[0-9]+)\b"

while command != "Purchase":
    matches = re.finditer(pattern, command)
    for match in matches:
        if match:
            furniture = match.group("furniture")
            price = match.group("price")
            quantity = match.group("quantity")

            furniture_bought.append(furniture)
            total_cost += float(price) * int(quantity)

    command = input()

print("Bought furniture:")

for current_furniture in furniture_bought:
    print(current_furniture)

print(f"Total money spend: {total_cost:.2f}")
