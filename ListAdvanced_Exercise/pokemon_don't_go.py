pokemons = list(map(int, input().split()))

removed_elements = []

while True:
    if not pokemons:
        break

    index = int(input())

    if index < 0:
        val_of_removed_elem = pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index >= len(pokemons):
        val_of_removed_elem = pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        val_of_removed_elem = pokemons.pop(index)

    indices_of_smaller_elements = [x for x in range(len(pokemons)) if pokemons[x] <= val_of_removed_elem]
    indices_of_greater_elements = [x for x in range(len(pokemons)) if pokemons[x] > val_of_removed_elem]

    for idx in indices_of_smaller_elements:
        pokemons[idx] += val_of_removed_elem

    for idx in indices_of_greater_elements:
        pokemons[idx] -= val_of_removed_elem

    removed_elements.append(val_of_removed_elem)

print(sum(removed_elements))
