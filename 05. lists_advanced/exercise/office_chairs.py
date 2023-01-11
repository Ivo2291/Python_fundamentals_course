number_of_rooms = int(input())
free_chairs = 0
chairs_are_enough = True

for room_number in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()
    visitors = int(visitors)

    difference = abs(len(chairs) - visitors)

    if len(chairs) < visitors:
        print(f"{difference} more chairs needed in room {room_number}")
        chairs_are_enough = False
    else:
        free_chairs += difference

if chairs_are_enough:
    print(f"Game On, {free_chairs} free chairs left")

# second_solution

number_of_rooms = int(input())
total_free_chairs = 0
chairs_are_enough = True

for room in range(1, number_of_rooms + 1):
    room_info = input().split()
    chairs = room_info[0]
    visitors = int(room_info[1])
    needed_chairs = visitors - len(chairs)

    if visitors > len(chairs):
        chairs_are_enough = False
        print(f"{needed_chairs} more chairs needed in room {room}")
    else:
        free_chairs = abs(needed_chairs)
        total_free_chairs += free_chairs

if chairs_are_enough:
    print(f"Game On, {total_free_chairs} free chairs left")
