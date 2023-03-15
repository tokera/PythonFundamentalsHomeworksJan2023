import re

racers = input().split(", ")
name_pattern = r"[A-Za-z]"
digit_pattern = r"[0-9]"
ranking = ["1st", "2nd", "3rd"]
racers_as_dict = {}

command = input()
while command != "end of race":

    letter_match = re.findall(name_pattern, command)
    digit_match = re.findall(digit_pattern, command)

    name = "".join(letter_match)
    score = sum([int(x) for x in digit_match])

    if name in racers:
        if name not in racers_as_dict:
            racers_as_dict[name] = 0

        racers_as_dict[name] += score

    command = input()

if racers_as_dict:
    counter = 0
    for idx, pvk in enumerate(sorted(racers_as_dict.items(), key=lambda x: (-x[1]))):
        if counter == 3:
            break
        print(f"{ranking[idx]} place: {pvk[0]}")
        counter += 1
