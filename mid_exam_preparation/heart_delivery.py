neighborhood = [int(house) for house in input().split("@")]
command = input().split()
cupid_position = 0

while command[0] != "Love!":
    length_of_jump = int(command[1])
    cupid_position += length_of_jump

    if cupid_position >= len(neighborhood):
        cupid_position = 0
    neighborhood[cupid_position] -= 2

    if neighborhood[cupid_position] <= -2:
        print(f"Place {cupid_position} already had Valentine's day.")

    elif neighborhood[cupid_position] <= 0:
        print(f"Place {cupid_position} has Valentine's day.")

    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

failed_houses = [house for house in neighborhood if house > 0]

if failed_houses:
    print(f"Cupid has failed {len(failed_houses)} places.")
else:
    print("Mission was successful.")
