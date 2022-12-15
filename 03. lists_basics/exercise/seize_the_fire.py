fire_cells = input().split("#")
water = int(input())

total_fire = 0
effort = 0
condition = False

print("Cells:")

for current_fire in fire_cells:
    fire_info = current_fire.split(" = ")
    type_of_fire = fire_info[0]
    value_of_fire = int(fire_info[1])
    condition = False

    if type_of_fire == "High":
        if 81 <= value_of_fire <= 125:
            condition = True

    elif type_of_fire == "Medium":
        if 51 <= value_of_fire <= 80:
            condition = True

    elif type_of_fire == "Low":
        if 1 <= value_of_fire <= 50:
            condition = True

    if condition:
        if water >= value_of_fire:
            water -= value_of_fire
            effort += value_of_fire * 0.25
            total_fire += value_of_fire
            print(f"- {value_of_fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

# second_solution

fire_info = input().split("#")
water = int(input())
effort = 0
cell_list = []
cell_is_valid = False

for fire in fire_info:
    current_fire = fire.split(" = ")
    type_of_fire = current_fire[0]
    value_of_cell = int(current_fire[1])

    if value_of_cell > water:
        continue

    if type_of_fire == "High":
        if 81 <= value_of_cell <= 125:
            cell_is_valid = True

    elif type_of_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            cell_is_valid = True

    elif type_of_fire == "Low":
        if 1 <= value_of_cell <= 50:
            cell_is_valid = True

    if cell_is_valid:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        cell_list.append(value_of_cell)
    cell_is_valid = False

total_fire = sum(cell_list)

print("Cells:")

for cell in range(len(cell_list)):
    print(f" - {cell_list[cell]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
