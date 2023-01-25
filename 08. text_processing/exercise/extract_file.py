path = input().split("\\")
info = path[-1].split(".")

file_name = info[0]
file_extension = info[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
