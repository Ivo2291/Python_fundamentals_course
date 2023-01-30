targets = list(map(int, input().split()))
shot_targets = 0
command = input()

while command != "End":
    index = int(command)

    if 0 <= index < len(targets):
        current_value = targets[index]

        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_value:
                    targets[i] -= current_value
                else:
                    targets[i] += current_value

        targets[index] = -1
        shot_targets += 1

    command = input()

targets = list(map(str, targets))

print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")
