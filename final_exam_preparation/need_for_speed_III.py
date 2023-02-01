number_of_cars = int(input())
cars_data_dict = {}

for cars in range(number_of_cars):
    my_car, my_mileage, my_fuel = input().split("|")
    cars_data_dict[my_car] = [int(my_mileage), int(my_fuel)]

command = input()

while command != "Stop":
    split_command = command.split(" : ")
    current_command = split_command[0]
    current_car = split_command[1]

    if current_command == "Drive":
        distance = int(split_command[2])
        fuel = int(split_command[3])

        if fuel > cars_data_dict[current_car][1]:
            print(f"Not enough fuel to make that ride")

        else:
            cars_data_dict[current_car][0] += distance
            cars_data_dict[current_car][1] -= fuel
            print(f"{current_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars_data_dict[current_car][0] >= 100000:
                del cars_data_dict[current_car]
                print(f"Time to sell the {current_car}!")

    elif current_command == "Refuel":
        fuel = int(split_command[2])

        if cars_data_dict[current_car][1] + fuel > 75:
            fuel = 75 - cars_data_dict[current_car][1]
            cars_data_dict[current_car][1] = 75

        else:
            cars_data_dict[current_car][1] += fuel

        print(f"{current_car} refueled with {fuel} liters")

    elif current_command == "Revert":
        kilometers = int(split_command[2])

        if cars_data_dict[current_car][0] - kilometers < 10000:
            cars_data_dict[current_car][0] = 10000

        else:
            cars_data_dict[current_car][0] -= kilometers
            print(f"{current_car} mileage decreased by {kilometers} kilometers")

    command = input()

for key, value in cars_data_dict.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")

# second_solution

# number_of_lines = int(input())
# cars_dict = {}
#
# for cars in range(number_of_lines):
#     car_info = input().split("|")
#     car = car_info[0]
#     mileage = int(car_info[1])
#     fuel = int(car_info[2])
#     cars_dict[car] = {"mileage": mileage, "fuel": fuel}
#
# command = input()
#
# while command != "Stop":
#     split_command = command.split(" : ")
#     current_command = split_command[0]
#     current_car = split_command[1]
#
#     if current_command == "Drive":
#         distance = int(split_command[2])
#         fuel = int(split_command[3])
#
#         if cars_dict[current_car]["fuel"] < fuel:
#             print("Not enough fuel to make that ride")
#
#         else:
#             cars_dict[current_car]["mileage"] += distance
#             cars_dict[current_car]["fuel"] -= fuel
#             print(f"{current_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#
#         if cars_dict[current_car]["mileage"] >= 100000:
#             print(f"Time to sell the {current_car}!")
#             del cars_dict[current_car]
#
#     elif current_command == "Refuel":
#         fuel = int(split_command[2])
#
#         if cars_dict[current_car]["fuel"] + fuel > 75:
#             fuel = 75 - cars_dict[current_car]["fuel"]
#
#         cars_dict[current_car]["fuel"] += fuel
#
#         print(f"{current_car} refueled with {fuel} liters")
#
#     elif current_command == "Revert":
#         kilometers = int(split_command[2])
#
#         cars_dict[current_car]["mileage"] -= kilometers
#
#         if cars_dict[current_car]["mileage"] < 10000:
#             cars_dict[current_car]["mileage"] = 10000
#
#         else:
#             print(f"{current_car} mileage decreased by {kilometers} kilometers")
#
#     command = input()
#
# for key, value in cars_dict.items():
#     print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
