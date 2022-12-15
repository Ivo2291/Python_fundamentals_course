cards_list = input().split(" ")
count_of_shuffles = int(input())
reordered_list = []

a = int((len(cards_list)) / 2)

for num in range(count_of_shuffles):
    for i in range(a):
        reordered_list.append(cards_list[i])
        b = int(a + i)
        reordered_list.append(cards_list[b])

    cards_list.clear()
    cards_list.extend(reordered_list)
    reordered_list.clear()

print(cards_list)

# second_solution

cards = input().split()
count_of_shuffles = int(input())
shuffled_deck = cards

for shuffle in range(count_of_shuffles):
    shuffled_deck = []
    middle_of_the_deck = len(cards) // 2
    left_half = cards[:middle_of_the_deck]
    right_half = cards[middle_of_the_deck:]

    for card_index in range(len(left_half)):
        shuffled_deck.append(left_half[card_index])
        shuffled_deck.append(right_half[card_index])
    cards = shuffled_deck

print(shuffled_deck)
