count_of_people = int(input())
lift_spaces = [int(spaces) for spaces in input().split()]

for index in range(len(lift_spaces)):
    wagon_fill = min(4 - lift_spaces[index], count_of_people)
    lift_spaces[index] += wagon_fill
    count_of_people -= wagon_fill

if count_of_people > 0:
    print(f"There isn't enough space! {count_of_people} people in a queue!")

elif len([wagon for wagon in lift_spaces if wagon < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(wag) for wag in lift_spaces]))
