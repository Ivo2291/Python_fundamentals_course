budget = int(input())
budget_is_enough = True

command = input()

while command != "End":
    product_price = int(command)

    if product_price > budget:
        budget_is_enough = False
        break
    else:
        budget -= product_price

    command = input()

if budget_is_enough:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")
