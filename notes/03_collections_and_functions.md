# Collections and function tools

## Representing records

A list stores an ordered sequence. A dictionary associates keys with values, such as a fictional student's name and marks. A list of dictionaries can represent multiple records.

A function packages reusable behavior. `return` passes a result to the caller; `print` displays a value.

## Transform, select, combine, and number

| Tool | Purpose | Detail to remember |
| --- | --- | --- |
| `map(function, values)` | Transform each item | Returns an iterator |
| `filter(predicate, values)` | Keep matching items | Returns an iterator of original matching items |
| `zip(first, second)` | Pair corresponding items | Stops at the shortest input by default |
| `enumerate(values, start=1)` | Produce index/value pairs | Useful for numbered displays |
| `lambda record: record["score"]` | Define a short expression function | Useful as a sorting key |
| `sorted(values, key=..., reverse=...)` | Return a new sorted list | Leaves original order unchanged |
| `values.sort(...)` | Sort a list in place | Changes the list and returns None |

Convert an iterator to a list when you want to display all its values together. Use `def` rather than a lambda for longer logic.

## Custom sorting

A key function chooses what to compare. `sorted(students, key=lambda student: student["score"], reverse=True)` sorts records from highest score to lowest.

A tuple key supports multiple sorting rules. Python's stable sorting preserves input order among items with equal keys. `operator.itemgetter` is another way to extract dictionary fields as sorting keys.

## Variable arguments and unpacking

In a function definition, `*values` collects positional arguments into a tuple, and `**details` collects keyword arguments into a dictionary. The parameter names are conventions.

At a call site, `*sequence` and `**mapping` unpack arguments. For example, `add_scores(*[10, 20, 30])` supplies three positional arguments.

## Run the illustrative example

`python3 exercises/session_review/function_tools.py` prints:

```text
Doubled: [2, 4, 6, 8]
Even: [2, 4]
Ranked: [(1, 'Sam'), (2, 'Alex')]
Original order: ['Alex', 'Sam']
Argument sum: 60
Keywords: {'topic': 'functions', 'status': 'review'}
```

Read [function_tools.py](../exercises/session_review/function_tools.py) to see these tools combined with fictional records.

Return to [topics studied](../PROGRESS.md).
