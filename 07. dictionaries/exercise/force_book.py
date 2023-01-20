command = input()
forces_dict = {}

while command != "Lumpawaroo":
    condition = True

    if "|" in command:
        side, user = command.split(" | ")

        for key, value in forces_dict.items():
            if user in value:
                condition = False
                break

        if condition:
            if side not in forces_dict:
                forces_dict[side] = [user]

            elif side in forces_dict and user not in forces_dict[side]:
                forces_dict[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")

        for k, v in forces_dict.items():
            if user in v:
                v.remove(user)
                break

        if side not in forces_dict:
            forces_dict[side] = [user]
            print(f"{user} joins the {side} side!")

        elif side in forces_dict and user not in forces_dict[side]:
            forces_dict[side].append(user)
            print(f"{user} joins the {side} side!")

    command = input()

for current_side, current_user in forces_dict.items():
    if forces_dict[current_side]:
        print(f"Side: {current_side}, Members: {len(forces_dict[current_side])}")
        for force_user in forces_dict[current_side]:
            print(f"! {force_user}")
