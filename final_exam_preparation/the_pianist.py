number_of_pieces = int(input())
pieces_dict = {}

for number in range(number_of_pieces):
    piece_name, composer, piece_key = input().split("|")
    pieces_dict[piece_name] = [composer, piece_key]

command = input()

while command != "Stop":
    split_command = command.split("|")
    current_command = split_command[0]
    current_piece = split_command[1]

    if current_command == "Add":
        current_composer = split_command[2]
        current_key = split_command[3]

        if current_piece not in pieces_dict:
            pieces_dict[current_piece] = [current_composer, current_key]
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
        else:
            print(f"{current_piece} is already in the collection!")

    elif current_command == "Remove":

        if current_piece in pieces_dict:
            del pieces_dict[current_piece]
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    elif current_command == "ChangeKey":
        new_key = split_command[2]

        if current_piece in pieces_dict:
            pieces_dict[current_piece][1] = new_key
            print(f"Changed the key of {current_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    command = input()

for key, value in pieces_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
