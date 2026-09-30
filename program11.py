def grade(marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"


name = input("Name: ")
marks = [float(input("Mark: ")) for _ in range(3)]

print("Student:", name)
print("Average:", sum(marks) / 3)
print("Grade:", grade(marks))