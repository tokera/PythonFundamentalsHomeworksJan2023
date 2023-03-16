import re

destination = {}
places_on_the_map = input()

pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"

result = re.findall(pattern, places_on_the_map)
for item in result:
    destination[item[1]] = len(item[1])

print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {sum(destination.values())}")
