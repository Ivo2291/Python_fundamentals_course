import re

text = input()
total_calories = 0
names_list = []
dates_list = []
calories_list = []
pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
matches = re.finditer(pattern, text)

for match in matches:
    name = match.group(2)
    expiration_date = match.group(3)
    calories = match.group(4)
    total_calories += int(calories)
    names_list.append(name)
    dates_list.append(expiration_date)
    calories_list.append(calories)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for i in range(len(names_list)):
    print(f"Item: {names_list[i]}, Best before: {dates_list[i]}, Nutrition: {calories_list[i]}")

# second_solution
#
# import re
#
# text = input()
#
# pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
# matches = re.findall(pattern, text)
# calories = 0
# items = []
#
# for match in matches:
#     current_item = [el for el in match]
#     items.append(current_item)
#     calories += int(current_item[3])
#
# days_last = calories // 2000
#
# print(f"You have food to last you for: {days_last} days!")
#
# for item in items:
#     print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")
