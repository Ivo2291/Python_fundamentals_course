def grade_text(some_grade):
    if some_grade < 3:
        return "Fail"
    elif some_grade < 3.5:
        return "Poor"
    elif some_grade < 4.5:
        return "Good"
    elif some_grade < 5.5:
        return "Very Good"
    else:
        return "Excellent"


grade = float(input())
print(grade_text(grade))
