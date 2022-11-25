first_num = int(input())
second_num = int(input())
third_num = int(input())

if first_num > second_num and first_num > third_num:
    print(first_num)

if second_num > first_num and second_num > third_num:
    print(second_num)

if third_num > first_num and third_num > second_num:
    print(third_num)
