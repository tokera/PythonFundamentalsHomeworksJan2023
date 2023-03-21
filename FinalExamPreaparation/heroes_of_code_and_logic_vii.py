number_of_heroes = int(input())

all_heroes = {}

for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()

    all_heroes[hero_name] = {}
    all_heroes[hero_name]["hp"] = int(hp)
    all_heroes[hero_name]["mp"] = int(mp)

while True:
    command = input()
    if command == "End":
        break

    command_args = command.split(" - ")
    action = command_args[0]
    hero_name = command_args[1]

    if action == "CastSpell":
        mp_needed = int(command_args[2])
        spell_name = command_args[3]

        if all_heroes[hero_name]["mp"] < mp_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
            continue

        all_heroes[hero_name]["mp"] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name]['mp']} MP!")
    elif action == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]

        if all_heroes[hero_name]["hp"] <= damage:
            print(f"{hero_name} has been killed by {attacker}!")
            all_heroes.pop(hero_name)
            continue

        all_heroes[hero_name]["hp"] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {all_heroes[hero_name]['hp']} HP left!")
    elif action == "Recharge":
        amount = int(command_args[2])
        current_mp = all_heroes[hero_name]["mp"]

        if current_mp + amount > 200:
            all_heroes[hero_name]["mp"] = 200
            amount = 200 - current_mp
        else:
            all_heroes[hero_name]["mp"] += amount

        print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        amount = int(command_args[2])

        current_hp = all_heroes[hero_name]["hp"]

        if current_hp + amount > 100:
            all_heroes[hero_name]["hp"] = 100
            amount = 100 - current_hp
        else:
            all_heroes[hero_name]["hp"] += amount

        print(f"{hero_name} healed for {amount} HP!")

for hero, info in all_heroes.items():
    print(f"{hero}")
    print(f"  HP: {info['hp']}")
    print(f"  MP: {info['mp']}")
