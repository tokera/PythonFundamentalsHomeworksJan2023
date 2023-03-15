submissions = {}
users_by_total_points = {}

line = input()
while line != "no more time":
    username, contest, points = line.split(" -> ")

    if contest not in submissions:
        submissions[contest] = {}

    if username not in submissions[contest]:
        submissions[contest][username] = int(points)
    elif submissions[contest][username] < int(points):
        submissions[contest][username] = int(points)

    line = input()

for contest, users in submissions.items():
    for user in users:
        if user not in users_by_total_points:
            users_by_total_points[user] = int(submissions[contest][user])
        else:
            users_by_total_points[user] += int(submissions[contest][user])


for contest, users in submissions.items():
    print(f"{contest}: {len(users)} participants")
    numbering = 1
    for user, points in sorted(users.items(), key=lambda x: (-x[1], x[0])):
        print(f"{numbering}. {user} <::> {points}")
        numbering += 1

print("Individual standings:")
numbering = 1
for user, total_points in sorted(users_by_total_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{numbering}. {user} -> {total_points}")
    numbering += 1
