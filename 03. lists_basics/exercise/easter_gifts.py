gifts = input().split()
command = input()

while command != "No Money":

    if "OutOfStock" in command:
        out_of_stock_list = command.split()
        for index in range(len(gifts)):
            if gifts[index] == out_of_stock_list[1]:
                gifts[index] = "None"

    elif "Required" in command:
        required_list = command.split()
        if 0 <= int(required_list[2]) < len(gifts):
            gifts[int(required_list[2])] = required_list[1]

    elif "JustInCase" in command:
        just_in_case_list = command.split()
        index = len(gifts)
        gifts[index - 1] = just_in_case_list[1]

    command = input()

for element in gifts:
    if element != "None":
        print(element, end=" ")
