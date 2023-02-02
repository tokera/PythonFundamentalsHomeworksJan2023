number_of_electrons = int(input())

atom_shells = []
current_shell = 1

while number_of_electrons > 0:
    max_electrons_in_current_shell = 2 * current_shell ** 2
    if number_of_electrons - max_electrons_in_current_shell >= 0:
        number_of_electrons -= max_electrons_in_current_shell
        atom_shells.append(max_electrons_in_current_shell)
    else:
        atom_shells.append(number_of_electrons)
        number_of_electrons = 0

    current_shell += 1

print(atom_shells)
