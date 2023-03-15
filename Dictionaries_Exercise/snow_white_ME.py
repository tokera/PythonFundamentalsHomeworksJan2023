colour_by_names = {}
dwarfs_list = []

while True:
    command_line = input()
    if command_line == "Once upon a time":
        break

    name, hat_colour, physics = command_line.split(" <:> ")

    if hat_colour not in colour_by_names:
        colour_by_names[hat_colour] = {}

    if name not in colour_by_names[hat_colour]:
        colour_by_names[hat_colour][name] = int(physics)
    elif colour_by_names[hat_colour][name] < int(physics):
        colour_by_names[hat_colour][name] = int(physics)

for hat_colour in colour_by_names:
    for name, physics in colour_by_names[hat_colour].items():
        dwarfs_list.append({
            "length": len(colour_by_names[hat_colour]),
            "hat_colour": hat_colour,
            "name": name,
            "physics": physics})

for dwarf in sorted(dwarfs_list, key=lambda x: (-x["physics"], -x["length"])):
    print(f"({dwarf['hat_colour']}) {dwarf['name']} <-> {dwarf['physics']}")
