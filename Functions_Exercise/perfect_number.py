number = int(input())


def is_perfect_number(num):
    divisors = []
    result = ""
    if num > 0:
        for n in range(num, 1, -1):
            if num % n == 0:
                divisors.append(num / n)

        if sum(divisors) == num:
            result = "We have a perfect number!"
        else:
            result = "It's not so perfect."

    return result


print(is_perfect_number(number))
