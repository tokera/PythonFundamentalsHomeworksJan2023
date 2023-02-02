number = int(input())

is_prime = True

for n in range(2, (number // 2) + 1):
    if number % n == 0:
        is_prime = False
        break

print(is_prime)
