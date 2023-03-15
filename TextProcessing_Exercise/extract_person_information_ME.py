number_of_lines = int(input())

is_name_mode = False
is_age_mode = False

for _ in range(number_of_lines):
    text = input()
    name = ""
    age = ""

    for ch in text:
        if ch == "@":
            is_name_mode = True
            continue

        if ch == "#":
            is_age_mode = True
            continue

        if is_name_mode:
            if ch == "|":
                is_name_mode = False
                continue
            name += ch

        if is_age_mode:
            if ch == "*":
                is_age_mode = False
                continue
            age += ch

    print(f"{name} is {age} years old.")
