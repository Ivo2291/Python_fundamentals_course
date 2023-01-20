countries = input().split(", ")
cities = input().split(", ")

capitals = {key: value for key, value in zip(countries, cities)}

for country, city in capitals.items():
    print(f"{country} -> {city}")
