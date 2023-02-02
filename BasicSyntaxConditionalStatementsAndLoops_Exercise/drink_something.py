age = int(input())

print("drink", end=" ")

if age <= 14:
    print("toddy")
elif 15 <= age <= 18:
    print("coke")
elif 19 <= age <= 21:
    print("beer")
elif age > 21:
    print("whisky")
