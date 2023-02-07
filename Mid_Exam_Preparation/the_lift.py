people_waiting_for_lift = int(input())
current_state_of_lift = [int(x) for x in input().split()]
wagon_capacity = 4

while people_waiting_for_lift:
    if all(current_state_of_lift) == wagon_capacity:
        print(f"There isn't enough space! {people_waiting_for_lift} people in a queue!")
        print(" ".join(str(x) for x in current_state_of_lift))
        break

    for i in range(len(current_state_of_lift)):
        if current_state_of_lift[i] < wagon_capacity:
            people_to_fill_wagon = wagon_capacity - current_state_of_lift[i]
            if people_waiting_for_lift - people_to_fill_wagon < 0:
                current_state_of_lift[i] += people_waiting_for_lift
                people_waiting_for_lift = 0
                break
            people_waiting_for_lift -= people_to_fill_wagon
            current_state_of_lift[i] = wagon_capacity
else:
    print(" ".join(str(x) for x in current_state_of_lift))

print("The lift has empty spots!")
print(" ".join(str(x) for x in current_state_of_lift))
