inventory = input().split(", ")

command = input()
while command != "Craft!":
    command_args = command.split(" - ")
    action = command_args[0]
    item = command_args[1]

    if action == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        item_args = item.split(":")
        old_item = item_args[0]
        new_item = item_args[1]

        if old_item in inventory:
            idx = inventory.index(old_item)

            if idx == len(inventory) - 1:
                inventory.append(new_item)
            else:
                inventory.insert(idx + 1, new_item)
    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))
