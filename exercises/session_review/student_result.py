"""Illustrative educational example prepared for this repository using fictional data."""


def calculate_result(marks_text, maximum_marks):
    marks = int(marks_text)
    if maximum_marks <= 0:
        raise ValueError("Maximum marks must be positive")
    if not 0 <= marks <= maximum_marks:
        raise ValueError("Marks must be between zero and maximum marks")
    percentage = marks / maximum_marks * 100
    result = "Pass" if percentage >= 40 else "Fail"
    return percentage, result


if __name__ == "__main__":
    percentage, result = calculate_result("83", 100)
    print("Name: Alex")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Result: {result}")
