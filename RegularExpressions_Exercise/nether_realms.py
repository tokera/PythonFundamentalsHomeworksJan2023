import re

demons = [x.strip() for x in input().split(",")]

pattern_matching_health = r"[^0-9+\-*\/.]"
pattern_matching_damage = r"([+\-]?([0]|[1-9][0-9]*)(\.[0-9]+)?)" #r"([+-]?[1-9]\d+(.\d+)?)"
demons_as_dict = {}

for demon in demons:

    if " " in demon:
        continue

    health_symbols = re.findall(pattern_matching_health, demon)
    damage_digits = re.findall(pattern_matching_damage, demon)
    multiply_or_divide = re.findall(r"[\*\/]", demon)

    health = 0
    damage = 0

    for ch in health_symbols:
        health += ord(ch)

    for dig in damage_digits:
        damage += float(dig[0])

    for sign in multiply_or_divide:
        if sign == "*":
            damage *= 2
            continue
        damage /= 2

    if demon not in demons_as_dict:
        demons_as_dict[demon] = []

    demons_as_dict[demon].append(health)
    demons_as_dict[demon].append(damage)

if all(demons_as_dict):
    [print(f"{name} - {specs[0]} health, {specs[1]:.2f} damage") for name, specs in sorted(demons_as_dict.items())]
