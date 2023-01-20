from collections import Counter

word = input()
my_dict = Counter(word)

for key, value in my_dict.items():
    if key != " ":
        print(f"{key} -> {value}")
