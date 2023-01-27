energy = int(input())
battles_counter = 0
energy_left = True
command = input()

while command != "End of battle":
    distance_of_enemy = int(command)
    if distance_of_enemy > energy:
        print(f"Not enough energy! Game ends with {battles_counter} won battles and {energy} energy")
        energy_left = False
        break

    else:
        energy -= distance_of_enemy
        battles_counter += 1

    if battles_counter % 3 == 0:
        energy += battles_counter

    command = input()

if energy_left:
    print(f"Won battles: {battles_counter}. Energy left: {energy}")
