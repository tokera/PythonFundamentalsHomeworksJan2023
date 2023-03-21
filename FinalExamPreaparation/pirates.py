city_by_population = {}
city_by_gold = {}

while True:
    command = input()
    if command == "Sail":
        break

    city, population, gold = command.split("||")

    if city not in city_by_population:
        city_by_population[city] = int(population)
        city_by_gold[city] = int(gold)
        continue

    city_by_population[city] += int(population)
    city_by_gold[city] += int(gold)

event = input()
while event != "End":

    event_args = event.split("=>")
    action = event_args[0]
    town = event_args[1]

    if action == "Plunder":
        killed_people = int(event_args[2])
        stolen_gold = int(event_args[3])

        city_by_population[town] -= killed_people
        city_by_gold[town] -= stolen_gold
        print(f"{town} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")

        if city_by_population[town] == 0 or city_by_gold[town] == 0:
            city_by_population.pop(town)
            city_by_gold.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        gold = int(event_args[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_by_gold[town] += gold

            print(f"{gold} gold added to the city treasury. {town} now has {city_by_gold[town]} gold.")

    event = input()

if city_by_population:
    print(f"Ahoy, Captain! There are {len(city_by_population)} wealthy settlements to go to:")
    [print(f"{town} -> Population: {city_by_population[town]} citizens, Gold: {city_by_gold[town]} kg")
        for town in city_by_population]
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
