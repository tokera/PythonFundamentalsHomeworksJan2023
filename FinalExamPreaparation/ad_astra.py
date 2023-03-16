import re

food = input()

pattern = r"([#|])([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1"
result = re.findall(pattern, food)
calories = [int(x[-1]) for x in result]

print(f"You have food to last you for: {sum(calories) // 2000} days!")

for food in result:
    print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[-1]}")
