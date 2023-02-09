neighbourhood = [int(x) for x in input().split("@")]

command = input()
current_home = 0

while command != "Love!":
    command_args = command.split()
    jump_length = int(command_args[1])

    if current_home + jump_length < len(neighbourhood):
        current_home += jump_length
    else:
        current_home = 0

    if neighbourhood[current_home] - 2 == 0:
        neighbourhood[current_home] -= 2
        print(f"Place {current_home} has Valentine's day.")
    elif neighbourhood[current_home] == 0:
        print(f"Place {current_home} already had Valentine's day.")
    else:
        neighbourhood[current_home] -= 2

    command = input()

print(f"Cupid's last position was {current_home}.")

cupid_failed_houses = [x for x in neighbourhood if x != 0]

if not cupid_failed_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(cupid_failed_houses)} places.")
