def print_tribonacci_seq(n):
    previous_three = [0, 0, 1]

    for i in range(n):
        sum_of_three = sum(previous_three)
        print(previous_three[-1], end=" ")

        previous_three[0], previous_three[1] = previous_three[1], previous_three[2]
        previous_three[2] = sum_of_three


number = int(input())

print_tribonacci_seq(number)
