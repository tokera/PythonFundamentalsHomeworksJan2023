from collections import deque

kids = deque(input().split())
n = int(input())
counter = 0

while len(kids) > 1:
    counter += 1
    current_kid = kids.popleft()
    if counter == n:
        print(f"Removed {current_kid}")
        counter = 0
    else:
        kids.append(current_kid)

print(f"Last is {kids[0]}")
