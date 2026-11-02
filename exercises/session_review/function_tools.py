"""Illustrative Level 1 collections and functions example using fictional marks."""


def analyze_marks(marks):
    if not marks:
        return {"total": 0, "average": 0, "passed": 0, "highest": None}

    total = sum(marks)
    passed = 0
    for mark in marks:
        if mark >= 40:
            passed += 1

    return {
        "total": total,
        "average": total / len(marks),
        "passed": passed,
        "highest": max(marks),
    }


if __name__ == "__main__":
    summary = analyze_marks([85, 35, 90, 40])
    print(f"Total: {summary['total']}")
    print(f"Average: {summary['average']:.2f}")
    print(f"Passed: {summary['passed']}")
    print(f"Highest: {summary['highest']}")
    print("Empty:", analyze_marks([]))
