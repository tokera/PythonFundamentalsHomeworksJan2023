population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

below_min_wealth = list(filter(lambda x: x < min_wealth, population))
above_min_wealth = list(filter(lambda y: y >= min_wealth, population))

needed_wealth = [min_wealth - x for x in below_min_wealth]

if (sum(above_min_wealth) - sum(needed_wealth)) >= (len(above_min_wealth) * min_wealth):
    below_min_wealth = [min_wealth for x in below_min_wealth]

    while needed_wealth:
        idx_of_needed_wealth = 0
        idx_of_max = above_min_wealth.index(max(above_min_wealth))

        if (above_min_wealth[idx_of_max] - needed_wealth[idx_of_needed_wealth]) >= 0:
            above_min_wealth[idx_of_max] -= needed_wealth[idx_of_needed_wealth]
            needed_wealth.pop(idx_of_needed_wealth)

    print(below_min_wealth + above_min_wealth)
else:
    print("No equal distribution possible")
