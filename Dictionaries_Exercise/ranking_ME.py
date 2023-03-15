contest_line = input()

ref_contests = {}
while contest_line != "end of contests":
    contest, password = contest_line.split(":")

    ref_contests[contest] = password

    contest_line = input()

users_by_contests = {}
submission_line = input()
while submission_line != "end of submissions":
    contest, password, username, points = submission_line.split("=>")

    if contest in ref_contests and ref_contests[contest] == password:
        if username not in users_by_contests:
            users_by_contests[username] = {}

        if contest not in users_by_contests[username]:
            users_by_contests[username][contest] = int(points)
        elif users_by_contests[username][contest] < int(points):
            users_by_contests[username][contest] = int(points)

    submission_line = input()

best_candidate = ""
max_points = 0

for user, contests in users_by_contests.items():
    current_points = 0
    for points in contests.values():
        current_points += points

    if current_points > max_points:
        best_candidate = user
        max_points = current_points

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")

sorted_users = sorted(list(users_by_contests.keys()))

for user in sorted_users:
    print(f"{user}")
    for contest, points in sorted(users_by_contests[user].items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
        print(f"#  {contest} -> {points}")
