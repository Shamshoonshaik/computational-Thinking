def calculate_grade(marks: list[float]) -> str:
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


# Test
assert calculate_grade([90, 90, 90]) == "A"

marks = [90, 90, 90]

print("Marks:", marks)
print("Average:", sum(marks) / len(marks))
print("Grade:", calculate_grade(marks))
print("All tests passed")