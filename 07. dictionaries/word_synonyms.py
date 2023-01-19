number = int(input())
dictionary = {}

for words in range(number):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for word in dictionary:
    synonyms = dictionary[word]
    print(f"{word} - {', '.join(synonyms)}")
