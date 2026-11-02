"""Illustrative educational example prepared for this repository using fictional data."""


def add_scores(*values):
    return sum(values)


def collect_details(**details):
    return details


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print("Doubled:", list(map(lambda number: number * 2, numbers)))
    print("Even:", list(filter(lambda number: number % 2 == 0, numbers)))
    students = [dict(name=name, score=score) for name, score in zip(
        ["Alex", "Sam"], [70, 90]
    )]
    ranked = sorted(students, key=lambda student: student["score"], reverse=True)
    print("Ranked:", list(enumerate([student["name"] for student in ranked], start=1)))
    print("Original order:", [student["name"] for student in students])
    print("Argument sum:", add_scores(*[10, 20, 30]))
    print("Keywords:", collect_details(topic="functions", status="review"))
