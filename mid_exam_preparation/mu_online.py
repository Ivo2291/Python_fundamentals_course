dungeons_rooms = input().split("|")
health = 100
bitcoins = 0
room_counter = 0
killed = False

for room in dungeons_rooms:
    current_room = room.split()
    command = current_room[0]
    number = int(current_room[1])
    room_counter += 1

    if command == "potion":
        if health + number > 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            killed = True
            break


if not killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
