def convert_to_round(some_list):
    rounded_list = []

    for num in some_list:
        current_num = float(num)
        rounded_list.append(round(current_num))

    return rounded_list


input_list = input().split(" ")
print(convert_to_round(input_list))
