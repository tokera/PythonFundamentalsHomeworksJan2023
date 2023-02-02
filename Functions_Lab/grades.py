def assessment(grade):
    result = ""

    if 2.0 <= grade <= 2.99:
        result = "Fail"
    elif 3.0 <= grade <= 3.49:
        result = "Poor"
    elif 3.5 <= grade <= 4.49:
        result = "Good"
    elif 4.5 <= grade <= 5.49:
        result = "Very Good"
    elif 5.5 <= grade <= 6:
        result = "Excellent"

    return result


input_grade = float(input())

print(assessment(input_grade))
