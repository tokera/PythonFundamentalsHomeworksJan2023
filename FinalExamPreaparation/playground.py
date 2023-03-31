def tower_breakers(n, m):
    return 2 if n % 2 == 0 or m == 1 else 1


t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]

    print(tower_breakers(n, m))

