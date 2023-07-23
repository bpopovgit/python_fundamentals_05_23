def check_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def check_containment(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def check_redundant_symbols(username):
    if " " in username:
        return False
    return True


def is_username_valid(username):
    if check_length(username) and check_containment(username) and check_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_username_valid(username):
        print(username)
