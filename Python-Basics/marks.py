def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total + 10


def calculate_percentage(marks):
    total = calculate_total(marks)
    return (total / (len(marks) * 100)) * 100


def is_passed(marks):
    percentage = calculate_percentage(marks)

    if percentage > 40:
        return True

    return False


def main():
    print("Student Marks System")

    marks = []

    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    print("\nTotal:", calculate_total(marks))
    print("Percentage:", calculate_percentage(marks))
    print("Passed:", is_passed(marks))


if __name__ == "__main__":
    main()