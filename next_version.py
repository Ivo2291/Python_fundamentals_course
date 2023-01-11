def next_version(old_version):
    old_version = int("".join(old_version)) + 1
    if old_version > 999:
        old_version = 999
    result = ".".join(str(old_version))
    return result


version = input().split(".")
print(next_version(version))

# second_solution

version = list(map(int, input().split(".")))
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1

print(".".join(str(s) for s in version))
