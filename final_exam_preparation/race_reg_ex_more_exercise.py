participants = input().split(", ")
text = input()
race_data_dict = {}
name = ""
distance = 0

while text != "end of race":
    for char in text:
        if char.isalnum():
            if char.isalpha():
                name += char
            else:
                distance += int(char)

    if name in participants:
        if name in race_data_dict:
            race_data_dict[name] += distance
        else:
            race_data_dict[name] = distance

    name = ""
    distance = 0

    text = input()

sorted_participants = sorted(race_data_dict.items(), key=lambda x: x[1], reverse=True)

name_list, kilometers_list = zip(*sorted_participants)

winners_list = []

for i in range(3):
    winners_list.append(name_list[i])

print(f"1st place: {winners_list[0]}")
print(f"2nd place: {winners_list[1]}")
print(f"3rd place: {winners_list[2]}")
