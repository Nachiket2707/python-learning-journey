# Collections and functions

## Choosing a collection

| Collection | Purpose | Example |
| --- | --- | --- |
| List | An ordered, changeable sequence | `[85, 35, 90, 40]` |
| Tuple | An ordered sequence whose entries cannot be reassigned | `("math", "science")` |
| Dictionary | Values associated with keys | `{"name": "Alex", "marks": 85}` |
| Set | Unique values, without a positional order | `{"math", "science"}` |

A list of dictionaries can represent multiple records, as in the [CSV example](exercises/session_review/file_formats.py). Square brackets create a list; `append(value)` adds an item to its end.

## Reusable functions

Define a function with `def`, give it a parameter, and indent its body. A parameter receives a value when the function is called. `return` passes a result back to the caller; `print` displays a value.

The illustrative [function_tools.py](exercises/session_review/function_tools.py) defines `analyze_marks(marks)`. It accepts a list, uses `sum()`, `len()`, and `max()`, and returns a dictionary containing a total, average, pass count, and highest mark.

A loop counts each mark greater than or equal to 40. That condition includes exactly 40.

## Handling an empty collection

Dividing by `len(marks)` would fail when the list is empty, and `max([])` has no highest value. The example checks for an empty list first and returns zero totals, a zero average, no passes, and `None` for the highest value.

This makes the function reusable without hardcoding a particular list.

## Run the complete illustrative example

`python3 exercises/session_review/function_tools.py` prints:

```text
Total: 250
Average: 62.50
Passed: 3
Highest: 90
Empty: {'total': 0, 'average': 0, 'passed': 0, 'highest': None}
```

The sample marks are fictional. The function returns data; the calling code formats it for display.

Return to [Level 1 topics studied](PROGRESS.md).
