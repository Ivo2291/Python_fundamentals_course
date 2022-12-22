words = input().split()
palindrome = input()
all_palindromes_found = []

for word in words:
    reversed_word = "".join(reversed(word))
    if reversed_word == word:
        all_palindromes_found.append(word)

sum_of_palindromes = all_palindromes_found.count(palindrome)

print(all_palindromes_found)
print(f"Found palindrome {sum_of_palindromes} times")
