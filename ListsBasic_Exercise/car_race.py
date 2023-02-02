numbers = list(map(int, input().split()))

finish_line = len(numbers) // 2

first_car_time = 0
second_car_time = 0
winner = ""
faster_time = 0

for i in range(finish_line):
    if numbers[i] == 0:
        first_car_time -= first_car_time * (20 / 100)
        continue
    first_car_time += numbers[i]

for i in range(len(numbers) - 1, finish_line, -1):
    if numbers[i] == 0:
        second_car_time -= second_car_time * (20 / 100)
        continue
    second_car_time += numbers[i]

if first_car_time < second_car_time:
    winner = "left"
    faster_time = first_car_time
else:
    winner = "right"
    faster_time = second_car_time

print(f"The winner is {winner} with total time: {faster_time:.1f}")
