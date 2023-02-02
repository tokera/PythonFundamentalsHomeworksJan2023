gifts_plan_to_buy = list(input().split())
command = input()

while command != "No Money":
    command_to_list = list(command.split())

    if command_to_list[0] == "OutOfStock":
        while gifts_plan_to_buy.__contains__(command_to_list[1]):
            gifts_plan_to_buy[gifts_plan_to_buy.index(command_to_list[1])] = "None"
    elif command_to_list[0] == "Required":
        index = int(command_to_list[2])
        if 0 <= index < len(gifts_plan_to_buy):
            gifts_plan_to_buy[index] = command_to_list[1]
    elif command_to_list[0] == "JustInCase":
        gifts_plan_to_buy[len(gifts_plan_to_buy) - 1] = command_to_list[1]

    command = input()

result = list(filter(lambda x: x != "None", gifts_plan_to_buy))

print(" ".join(result))
