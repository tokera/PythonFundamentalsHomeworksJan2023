countries = input().split(", ")
capitals = input().split(", ")

zipped = zip(countries, capitals)
dict_country_cap = {country: capital for country, capital in zipped}

[print(f"{country} -> {capital}") for country, capital in dict_country_cap.items()]
