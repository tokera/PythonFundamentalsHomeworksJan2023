def is_valid_password(password_for_validating):
    is_valid = True
    if len(password_for_validating) < 6 or len(password_for_validating) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    count_letters = 0
    count_digits = 0
    for char in password_for_validating:
        if char.isalpha():
            count_letters += 1
        elif char.isdigit():
            count_digits += 1

    if (count_letters + count_digits) != len(password_for_validating):
        print("Password must consist only of letters and digits")
        is_valid = False

    if count_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


password = input()

is_valid_password(password)
