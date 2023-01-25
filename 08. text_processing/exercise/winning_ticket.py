def ticket_validation(ticket):
    if len(ticket) != 20:
        print("invalid ticket")
        return True
    return False


def winning_ticket(ticket):
    winning_symbols = ["@", "#", "$", "^"]
    left_half = ticket[:10]
    right_half = ticket[10:]

    for symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            symbol_repetition = symbol * repetition

            if symbol_repetition in left_half and symbol_repetition in right_half:
                if repetition == 10:
                    print(f"ticket \"{ticket}\" - {len(ticket) / 2:.0f}{symbol} Jackpot!")
                    return True
                elif 6 <= repetition <= 9:
                    print(f"ticket \"{current_ticket}\" - {len(symbol_repetition)}{symbol}")
                    return True

    print(f"ticket \"{current_ticket}\" - no match")


tickets = [element.strip() for element in input().split(", ")]

for current_ticket in tickets:
    if ticket_validation(current_ticket):
        continue

    winning_ticket(current_ticket)
