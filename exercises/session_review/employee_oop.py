"""Illustrative educational example prepared for this repository using fictional data."""


class Employee:
    company = "Learning Demo"

    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def increase_salary(self, percentage):
        if percentage < 0:
            raise ValueError("Percentage cannot be negative")
        self.salary += self.salary * percentage / 100


if __name__ == "__main__":
    employee = Employee("Alex", 35000)
    other_employee = Employee("Sam", 45000)
    employee.increase_salary(10)
    print(f"Alex monthly: {employee.salary:.2f}")
    print(f"Alex annual: {employee.annual_salary():.2f}")
    print(f"Sam monthly: {other_employee.salary:.2f}")
    print(f"Company: {Employee.company}")
