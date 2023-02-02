number_of_rooms = int(input())

is_enough_chairs = True
free_chairs = 0

for nr_room in range(1, number_of_rooms + 1):
    room = input().split()
    chairs = len(room[0])
    visitors = int(room[1])

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {nr_room}")
        is_enough_chairs = False
        continue

    free_chairs += (chairs - visitors)

if is_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
    