all_people = input().split()
k = int(input())

killed_people = []
current_i = 0
counter = 1

while len(all_people):
    if current_i >= len(all_people):
        current_i = 0

    if counter == k:
        killed_people.append(all_people[current_i])
        del all_people[current_i]
        counter = 1
    else:
        counter += 1
        current_i += 1

print("[" + ",".join(killed_people) + "]")
