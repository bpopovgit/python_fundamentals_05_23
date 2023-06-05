def validate_password(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


new_password = input()
password_is_valid = validate_password(new_password)
if password_is_valid:
    print("Password is valid")
