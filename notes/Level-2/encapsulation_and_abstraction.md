# Encapsulation and Abstraction

**Python Level 2 — Module 3**

This note introduces two ways to make object-oriented programs easier to use and safer to change. The examples are educational illustrations for this repository.

## Encapsulation

Encapsulation groups an object’s data with the methods that manage it. A class can validate changes so its data stays in a valid state.

Python uses naming conventions rather than strict access controls:
- `balance` is a public attribute intended for normal use.
- `_balance` signals an implementation detail by convention.
- `__balance` triggers name mangling to help avoid accidental name clashes. It is not a security boundary.

### Validate changes with a property

A property provides attribute syntax while allowing the class to control updates.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # Uses the setter for validation

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

account = BankAccount("Alex", 500)
account.deposit(100)
print(account.balance)
```

**Output:** `600`

The balance is stored in `_balance`; the public property checks values before accepting them. Python’s underscore is a convention, so code should use the public interface instead of changing `_balance` directly.

## Abstraction

Abstraction exposes the operations callers need while hiding implementation details. Python’s `abc` module can define an abstract base class that specifies operations a concrete subclass must implement.

### A payment interface

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process a payment and return a confirmation."""
        raise NotImplementedError

class UpiPayment(PaymentMethod):
    def pay(self, amount):
        return f"UPI payment received: ₹{amount}"

class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Card payment received: ₹{amount}"

def checkout(method, amount):
    print(method.pay(amount))

checkout(UpiPayment(), 500)
checkout(CardPayment(), 750)
```

**Output:**
```text
UPI payment received: ₹500
Card payment received: ₹750
```

`checkout()` depends on the shared `pay()` interface. Each payment class decides how to implement it. Because `PaymentMethod` has an abstract method, it cannot be instantiated until a subclass provides that method.

## Encapsulation and abstraction together

| Concept | Main idea |
| --- | --- |
| Encapsulation | Keep state and the methods that manage it together; validate changes through a clear interface. |
| Abstraction | Show callers what an object can do while hiding the details of how it does it. |

Both help make code easier to maintain: callers rely on a small, clear interface, while each class controls its own implementation.

## Further reading

- [Python `property` documentation](https://docs.python.org/3/library/functions.html#property)
- [Python abstract base classes documentation](https://docs.python.org/3/library/abc.html)
