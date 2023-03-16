import re

count_of_messages = int(input())

pattern_for_decrypting = r"[star]"
pattern_for_planet_info = r"@([A-Za-z]+)([^@\-!:>]+)?:(\d+)([^@\-!:>]+)?!([AD])!([^@\-!:>]+)?->(\d+)"
planets = {"A": [], "D": []}

for _ in range(count_of_messages):
    message = input()

    decrypted_key = re.findall(pattern_for_decrypting, message, re.IGNORECASE)

    decrypted_message_as_list = []
    for ch in message:
        decrypted_message_as_list.append(chr(ord(ch) - len(decrypted_key)))

    decrypted_message = "".join(decrypted_message_as_list)
    planet_info = re.findall(pattern_for_planet_info, decrypted_message)

    if not planet_info:
        continue

    planet_name = planet_info[0][0]
    attack_type = planet_info[0][4]

    planets[attack_type].append(planet_name)

for attack, name in planets.items():
    if attack == "A":
        print(f"Attacked planets: ", end="")
    else:
        print(f"Destroyed planets: ", end="")
    print(f"{len(planets[attack])}")
    [print(f"-> {name}") for name in sorted(planets[attack])]
