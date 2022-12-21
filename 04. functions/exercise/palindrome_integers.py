def palindrome_check(some_list):
    for number in some_list:
        if number == number[::-1]:
            print(True)
        else:
            print(False)


list_of_integers = input().split(", ")
palindrome_check(list_of_integers)
