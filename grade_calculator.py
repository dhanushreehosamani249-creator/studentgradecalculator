
def validate_marks(marks):
    if not marks:
        raise ValueError("Enter marks for at least one subject.")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")

    return True


def average(marks):
    validate_marks(marks)
    return sum(marks) / len(marks)


def grade(avg):
    if avg < 0 or avg > 100:
        raise ValueError("Average must be between 0 and 100.")

    if avg >= 90:
        return "A"
    if avg >= 75:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 35:
        return "D"

    return "F"


def is_pass(marks):
    validate_marks(marks)
    return all(mark >= 35 for mark in marks)


def main():
    name = input("Enter student name: ")
    count = int(input("Enter number of subjects: "))

    if count <= 0:
        print("Number of subjects must be positive.")
        return

    marks = []

    for i in range(count):
        marks.append(float(input(f"Enter marks for subject {i + 1}: ")))

    avg = average(marks)
    result = "PASS" if is_pass(marks) else "FAIL"

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Marks:", marks)
    print(f"Average: {avg:.2f}")
    print("Grade:", grade(avg))
    print("Result:", result)


if __name__ == "__main__":
    main()
