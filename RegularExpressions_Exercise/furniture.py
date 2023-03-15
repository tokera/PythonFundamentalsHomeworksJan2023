import re

furniture = input()
pattern = r">>([A-Za-z0-9]+)<<(\d+(\.\d+)?)!(\d+)"
all_furniture = []
while furniture != "Purchase":
    match = re.findall(pattern, furniture)
    all_furniture.append(match)

    furniture = input()

total_sum = 0
print(f"Bought furniture:")
for item in all_furniture:
    if not item:
        continue
    print(f"{item[0][0]}")
    total_sum += float(item[0][1]) * int(item[0][-1])

print(f"Total money spend: {total_sum:.2f}")
