# Level 2: Object-Oriented Programming

## Classes and objects

A class defines shared structure and behavior. An object is an instance of that class. Each employee object can hold its own name and salary, while methods keep related operations with that data.

- `__init__` initializes instance attributes when an instance is created.
- `self` refers to the particular instance receiving a method call; it is a naming convention.
- `employee.annual_salary()` uses that employee's salary.
- One instance method can call another through `self`.
- An instance attribute such as `self.salary` belongs to an individual object.
- A class attribute such as `company` is found on the class when not overridden on the instance.

Mutable class attributes can unintentionally share changing data. Per-object lists usually belong in `__init__`.

## OOP vocabulary

| Concept | Meaning |
| --- | --- |
| Encapsulation | Group related data and operations behind a useful interface |
| Inheritance | Define a specialized class based on another class |
| Polymorphism | Use a common interface with different object types |
| Abstraction | Expose essential behavior while hiding implementation details |

These definitions provide context for organizing larger programs.

## Employee example

Run `python3 exercises/session_review/employee_oop.py`:

```text
Alex monthly: 38500.00
Alex annual: 462000.00
Sam monthly: 45000.00
Company: Learning Demo
```

The illustrative [Employee class](../exercises/session_review/employee_oop.py) applies a 10% increase to a fictional monthly salary of 35000. The second employee's salary remains separate. Negative salaries and negative increases raise `ValueError`.

## Applying the design to other records

A student class can group a name and subject marks with methods for totals, averages, and results. For marks 85, 90, and 78, the total is 253 and the average is 84.33. If passing requires every subject to be at least 40, use a per-subject rule rather than testing only the average.

An account class can similarly group an owner and balance with deposit and withdrawal methods. Validation can reject nonpositive transactions and withdrawals beyond the balance. Such examples illustrate object design using fictional data.

Return to [topics studied](../PROGRESS.md).
