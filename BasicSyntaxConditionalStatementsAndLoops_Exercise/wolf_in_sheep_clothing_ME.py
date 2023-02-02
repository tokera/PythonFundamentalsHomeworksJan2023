# animals = input().split(", ")
#
# nr_of_sheep = 0
#
# if animals.index("wolf") == len(animals) - 1:
#     print("Please go away and stop eating my sheep")
# else:
#     nr_of_sheep = (len(animals) - animals.index("wolf")) - 1
#     print(f"Oi! Sheep number {nr_of_sheep}! You are about to be eaten by a wolf!")
#

animals = input()

wolf_location = animals.index('wolf')

if wolf_location == len(animals) - 4:
    print('Please go away and stop eating my sheep')
else:
    threatened_sheep = (len(animals) - (wolf_location + 4)) // 7
    print(f'Oi! Sheep number {threatened_sheep}! You are about to be eaten by a wolf!')
