n = int(input())
parking = {}
for _ in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        license_plate = command[2]
        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

[print(f"{user} => {plate_num}") for user, plate_num in parking.items()]
