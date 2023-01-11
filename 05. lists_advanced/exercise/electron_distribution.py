def electron_distribution(number):
    filled_shells = []
    shell_position = 1

    while True:
        element = 2 * (shell_position ** 2)
        if element < number:
            filled_shells.append(element)
            number -= element
        else:
            filled_shells.append(number)
            break

        shell_position += 1

    print(filled_shells)


data = int(input())
electron_distribution(data)

# second_solution

number_of_electrons = int(input())
filled_shells = []

for shell in range(1, number_of_electrons + 1):
    current_shell = 2 * (shell ** 2)

    if current_shell < number_of_electrons:
        filled_shells.append(current_shell)
        number_of_electrons -= current_shell
    else:
        filled_shells.append(number_of_electrons)
        break

print(filled_shells)
