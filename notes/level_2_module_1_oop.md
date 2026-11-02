# Level 2 — Module 1: Object-Oriented Programming

[Back to the topic overview](../PROGRESS.md) · [Repository home](../README.md)

## Classes and objects

Object-oriented programming (OOP) groups related data and behavior. A **class** defines a kind of object; an **object** (or instance) is one particular value created from that class. A Student class can describe many students, each with their own name and scores.

An **attribute** stores data on an object or class. A **method** is a function defined in a class that provides behavior. In the complete example below, Student is the class, maya and arjun refer to separate objects, name and scores are instance attributes, and average() is an instance method.

## Initializing an object with `__init__`

Calling Student("Maya") creates an instance and automatically runs its `__init__` method to initialize it. `__init__` sets the starting attributes; it must return None (normally by having no return statement). It initializes an already-created object.

Each call creates a new scores list, so one student's scores stay separate from another student's scores.

## Understanding self and instance methods

self refers to the instance receiving a method call. Python supplies this first argument automatically: maya.add_score(80) calls Student.add_score(maya, 80). The name self is a strong Python convention.

Use self.name to access that object's name and self.scores to access its scores. A parameter such as score is local to the method call. An instance method can update the object's state, return a result, or both. average() returns a value without changing the scores; add_score() changes the scores.

## Instance attributes and class attributes

| Kind | Defined in this example | Meaning |
| --- | --- | --- |
| Instance attribute | self.name and self.scores inside `__init__` | Each student has their own values |
| Class attribute | school_name in the class body | A shared default available through the class and its instances |

When an instance has no attribute of its own with a given name, lookup can find the class attribute. Changing Student.school_name changes the value seen by both students in this example. Assigning maya.school_name would instead create an instance attribute that shadows the shared value for Maya.

Keep per-object mutable data such as scores on the instance. Defining scores = [] in the class body would create one shared list; appending through either instance could affect both students.

## Complete illustrative example

This AI-generated educational example uses fictional students. It is provided for study and explanation; it is not presented as a learner-authored program or evidence of assessed completion.

Save the entire code block as student_oop.py, then run:

```bash
python3 student_oop.py
```

On Windows, use py if python3 is unavailable. Python 3 is sufficient; no packages, input files, or network access are needed.

```python
class Student:
    school_name = "Python Learning Academy"

    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            raise TypeError("Score must be a number.")
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def summary(self):
        return (
            f"{self.name} | {self.school_name} | "
            f"Scores: {self.scores} | Average: {self.average():.1f}"
        )


def main():
    maya = Student("Maya")
    arjun = Student("Arjun")

    print("Before adding scores:")
    print(maya.summary())
    print(arjun.summary())

    maya.add_score(80)
    maya.add_score(90)
    arjun.add_score(70)

    print("\nAfter adding scores:")
    print(maya.summary())
    print(arjun.summary())

    Student.school_name = "Community Python Academy"
    print("\nAfter changing the class attribute:")
    print(maya.summary())
    print(arjun.summary())

    try:
        maya.add_score(110)
    except ValueError as error:
        print(f"\nInvalid score: {error}")


if __name__ == "__main__":
    main()
```

### Expected output

```text
Before adding scores:
Maya | Python Learning Academy | Scores: [] | Average: 0.0
Arjun | Python Learning Academy | Scores: [] | Average: 0.0

After adding scores:
Maya | Python Learning Academy | Scores: [80, 90] | Average: 85.0
Arjun | Python Learning Academy | Scores: [70] | Average: 70.0

After changing the class attribute:
Maya | Community Python Academy | Scores: [80, 90] | Average: 85.0
Arjun | Community Python Academy | Scores: [70] | Average: 70.0

Invalid score: Score must be between 0 and 100.
```

## Walk through the example

1. Two calls to Student create two independent objects. `__init__` assigns each name and a fresh list.
2. summary() calls average(). An empty list produces 0.0 here by design, avoiding division by zero.
3. add_score() validates a value before appending it. Maya receives two scores; Arjun receives one.
4. Updating Student.school_name changes the shared class attribute. Both summaries show the new school.
5. A score of 110 raises ValueError before the list changes. The caller catches it and prints a clear message.
6. The main guard runs the demonstration when the file is executed directly. Importing it defines the class and function without running the demonstration.

## Explain it in your own words

- Which lines define a class, and which lines create objects?
- Why does adding a score to Maya leave Arjun's scores unchanged?
- How does self identify the student affected by add_score()?
- Why do both students show the new school name?
- What happens when average() is called before scores are added?

[Official Python tutorial: Classes](https://docs.python.org/3/tutorial/classes.html)

