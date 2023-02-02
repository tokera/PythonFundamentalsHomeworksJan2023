population = list(map(int, input().split(", ")))
min_wealth = int(input())

under_min_wealth_population = list(filter(lambda x: x < min_wealth, population))
above_min_wealth_population = list(filter(lambda y: y >= min_wealth, population))

needed_wealth = (min_wealth * len(under_min_wealth_population)) - sum(under_min_wealth_population)
result = []

if (sum(above_min_wealth_population) - needed_wealth) >= (len(above_min_wealth_population) * min_wealth):
    result = [min_wealth] * len(under_min_wealth_population)

while needed_wealth == 0:
    idx = above_min_wealth_population.index(max(above_min_wealth_population))

    if above_min_wealth_population[idx] - needed_wealth >= min_wealth:
        above_min_wealth_population[idx] -= needed_wealth
        needed_wealth = 0
    else:
        needed_wealth -= above_min_wealth_population[idx] - min_wealth
        above_min_wealth_population[idx] = min_wealth

print(result + above_min_wealth_population)




