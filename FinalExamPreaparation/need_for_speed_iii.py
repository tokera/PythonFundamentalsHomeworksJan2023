MAX_MILLAGE_FOR_CAR = 100000
MIN_MILLAGE_FOR_CAR = 10000
CAPACITY_OF_FUEL_TANK = 75

number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car, millage, fuel = input().split("|")

    cars[car] = {}
    cars[car]["distance"] = int(millage)
    cars[car]["fuel"] = int(fuel)

command = input()
while command != "Stop":
    command_args = command.split(" : ")
    action = command_args[0]
    car = command_args[1]

    if action == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])
        current_car_fuel = cars[car]["fuel"]
        if current_car_fuel < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["distance"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]["distance"] >= MAX_MILLAGE_FOR_CAR:
            cars.pop(car)
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        fuel = int(command_args[2])
        current_car_fuel = cars[car]["fuel"]

        if current_car_fuel + fuel > CAPACITY_OF_FUEL_TANK:
            fuel = CAPACITY_OF_FUEL_TANK - current_car_fuel
            current_car_fuel = CAPACITY_OF_FUEL_TANK
        else:
            current_car_fuel += fuel
        cars[car]["fuel"] = current_car_fuel
        print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometers = int(command_args[2])
        current_car_km = cars[car]["distance"]

        if current_car_km - kilometers >= MIN_MILLAGE_FOR_CAR:
            print(f"{car} mileage decreased by {kilometers} kilometers")
            current_car_km -= kilometers
        else:
            current_car_km = MIN_MILLAGE_FOR_CAR
        cars[car]["distance"] = current_car_km
    command = input()

[print(f"{car} -> Mileage: {info['distance']} kms, Fuel in the tank: {info['fuel']} lt.")
 for car, info in cars.items()]
