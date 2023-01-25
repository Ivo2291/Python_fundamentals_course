def length_func(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def containing(username):
    for char in username:
        if not(char.isalnum() or char == "-" or char == "_"):
            return False
        return True


def redundant_symbols(username):
    for char in username:
        if char == " ":
            return False
        return True


def validation(username):
    if length_func(username) and containing(username) and redundant_symbols(username):
        return True


usernames = input().split(", ")

for user in usernames:
    if validation(user):
        print(user)
