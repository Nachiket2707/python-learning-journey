# Variables, conversion, conditions, and loops

## Variables and output

A variable refers to a value. Defining `marks = 85.5` stores a value; displaying it requires a call such as `print(f"Marks: {marks}")`. F-strings insert expressions inside braces. Use `\n` for a newline.

## Converting text into numbers

`"83"` is text, while `83` is an integer. `int("83")` produces an integer for arithmetic. Invalid integer text raises `ValueError`.

A percentage is `marks / maximum_marks * 100`. For a passing threshold of 40%, use `percentage >= 40` so exactly 40% passes. An `if` or `else` block uses a colon and an indented body.

Run the illustrative [student_result.py](exercises/session_review/student_result.py):

```bash
python3 exercises/session_review/student_result.py
```

```text
Name: Alex
Percentage: 83.00%
Result: Pass
```

The function accepts other maximum marks too: 80 out of 200 is 40%. It validates positive maximum marks and a score within the allowed range.

## Loops, counters, and accumulators

`range(1, 21)` generates integers from 1 through 20 because its stop value is excluded. `number % 2 == 0` selects even numbers.

A counter increases by one for each match. An accumulator increases by the value being added. The illustrative [even_numbers.py](exercises/session_review/even_numbers.py) prints:

```text
Sum of even numbers: 110
Total even numbers: 10
```

Run `python3 exercises/session_review/even_numbers.py`.

To collect matching values, create a list with square brackets and call `even.append(number)` inside the condition. Using `break` would end the loop early, so it is unnecessary when processing the entire range.

Return to [topics studied](PROGRESS.md).
