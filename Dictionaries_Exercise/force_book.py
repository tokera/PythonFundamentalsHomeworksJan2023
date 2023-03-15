def user_existing_in_users(user, users):
    for item in users:
        if user in item:
            return True
    return False


command = input()
sides = {}
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if force_side not in sides and not user_existing_in_users(force_user, sides.values()):
            sides[force_side] = []
            sides[force_side].append(force_user)
        elif not user_existing_in_users(force_user, sides.values()):
            sides[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        if user_existing_in_users(force_user, sides.values()):
            if force_side not in sides:
                sides[force_side] = []
            for side, users in sides.items():
                if force_user in users:
                    sides[side].remove(force_user)
            sides[force_side].append(force_user)
        elif force_side in sides and not user_existing_in_users(force_user, sides.values()):
            sides[force_side].append(force_user)
        else:
            sides[force_side] = []
            sides[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, members in sides.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")

# Solution with two dictionaries

# line = input()
# side_by_users = {}
# user_by_side = {}
# while line != "Lumpawaroo":
#     if "|" in line:
#         force_side, force_user = line.split(" | ")
#
#         if force_side not in side_by_users and force_user not in user_by_side:
#             side_by_users[force_side] = [force_user]
#             user_by_side[force_user] = force_side
#         elif force_user not in user_by_side:
#             side_by_users[force_side].append(force_user)
#             user_by_side[force_user] = force_side
#     else:
#         force_user, force_side = line.split(" -> ")
#
#         if force_side not in side_by_users and force_user not in user_by_side:
#             side_by_users[force_side] = [force_user]
#             user_by_side[force_user] = force_side
#         elif force_user in user_by_side:
#             old_side = user_by_side[force_user]
#             user_by_side[force_user] = force_side
#             side_by_users[old_side].remove(force_user)
#
#             if force_side not in side_by_users:
#                 side_by_users[force_side] = []
#
#             side_by_users[force_side].append(force_user)
#         else:
#             side_by_users[force_side].append(force_user)
#             user_by_side[force_user] = force_side
#
#         print(f"{force_user} joins the {force_side} side!")
#
#     line = input()
#
# for side, users in side_by_users.items():
#     if len(users) == 0:
#         continue
#     print(f"Side: {side}, Members: {len(users)}")
#     for user in users:
#         print(f"! {user}")
