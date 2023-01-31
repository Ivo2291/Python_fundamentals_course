import re

string_of_places = input()
pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, string_of_places)
total_points = 0
destinations = []

for match in matches:
    destinations.append(match.group(2))
    total_points += len(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")
