sequence_of_numbers = map(int, input().split())
even_numbers = filter(lambda number: number % 2 == 0, sequence_of_numbers)

print(list(even_numbers))
