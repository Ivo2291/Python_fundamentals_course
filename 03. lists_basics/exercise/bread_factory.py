events = input().split("|")

energy = 100
coins = 100
is_closed = False
item_to_order = ""

for event in events:
    current_event = event.split("-")
    command = current_event[0]
    event_points = int(current_event[1])

    if command == "rest":

        if energy + event_points > 100:
            energy = 100
            dif = 100 - energy
            print(f"You gained {dif} energy.")
        else:
            energy += event_points
            print(f"You gained {event_points} energy.")

        print(f"Current energy: {energy}.")

    elif command == "order":

        if energy >= 30:
            coins += event_points
            energy -= 30
            print(f"You earned {event_points} coins.")

        else:
            print(f"You had to rest!")
            energy += 50

    else:
        item_to_order = command

        if coins >= event_points:
            print(f"You bought {item_to_order}.")
            coins -= event_points
        else:
            is_closed = True
            break

if is_closed:
    print(f"Closed! Cannot afford {item_to_order}.")
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
