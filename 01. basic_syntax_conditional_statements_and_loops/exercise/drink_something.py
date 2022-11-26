age = int(input())
result_text = ""

if age <= 14:
    result_text = "drink toddy"
elif 14 < age <= 18:
    result_text = "drink coke"
elif 18 < age <= 21:
    result_text = "drink beer"
else:
    result_text = "drink whisky"

print(result_text)
