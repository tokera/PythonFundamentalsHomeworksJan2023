count_of_wagons = int(input())

train = [0 for x in range(count_of_wagons)]

command = input().split()

while not command[0] == "End":
    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    else:
        train[int(command[1])] -= int(command[2])

    command = input().split()

print(train)
