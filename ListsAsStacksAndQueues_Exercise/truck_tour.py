from collections import deque

number_of_petrol_pumps = int(input())

petrol_pumps = []

for _ in range(number_of_petrol_pumps):
    petrol_pumps.append([int(x) for x in input().split()])

queue_of_pumps = deque(petrol_pumps)
reference_pumps = queue_of_pumps.copy()
fuel_in_tank = 0
idx = 0

while queue_of_pumps:
    current_pump = queue_of_pumps.popleft()
    current_pump_litters = current_pump[0]
    distance_to_next_pump = current_pump[1]

    if ((current_pump_litters + fuel_in_tank) - distance_to_next_pump) >= 0:
        fuel_in_tank += current_pump_litters - distance_to_next_pump
        continue

    queue_of_pumps = reference_pumps.copy()
    idx += 1
    fuel_in_tank = 0
    for _ in range(idx):
        tmp = queue_of_pumps.popleft()
        queue_of_pumps.append(tmp)

print(idx)
