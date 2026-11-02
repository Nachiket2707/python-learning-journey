# Exceptions, paths, and file formats

File management lets a program save information to disk and read it later. Text, CSV, and JSON serve different storage needs.

## Exceptions

| Construct | Purpose |
| --- | --- |
| `try` | Run an operation that may fail |
| `except` | Handle a matching expected error |
| `else` | Run when the try block finishes without an exception |
| `finally` | Perform cleanup when control leaves the statement |
| `raise` | Deliberately signal an error |

Catch specific errors such as `ValueError` for invalid number conversion or `FileNotFoundError` for a missing file. A custom exception can inherit from `Exception` when callers need to distinguish a specific failure.

```python
class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0:
        raise InvalidScoreError("Score cannot be negative")
    return score


try:
    score = validate_score(85)
except InvalidScoreError as error:
    print(error)
else:
    print(f"Score: {score}")
finally:
    print("Validation finished")
```

This illustrative snippet prints `Score: 85` and then `Validation finished`.

## A path describes a location

`Path("practice") / "note.txt"` constructs an address. `mkdir()` creates a folder. Opening a path in write mode creates the file if needed and clears existing contents. `exists()` checks whether the path exists. A separate `touch()` is unnecessary before opening a file for writing.

Relative paths start from Python's current working directory, which can differ from the script's directory. `Path.cwd()` shows that location. Import `Path` with `from pathlib import Path`.

## Text modes and reading methods

| Mode | Purpose | Existing contents |
| --- | --- | --- |
| `r` | Read an existing file | Preserved; a missing file raises FileNotFoundError |
| `w` | Write a file | Cleared when opened |
| `a` | Append to the end | Preserved, with new text added |

Use `with ... as ...` to close files reliably and `encoding="utf-8"` for these text examples. Append adds to the end rather than replacing a value in the middle.

`read()` reads remaining contents, `readline()` reads one line, and `readlines()` collects remaining lines in a list. Iterating over the file processes it line by line.

## CSV: column definitions and write order

A list of dictionaries can represent student records. `csv.DictWriter(..., fieldnames=[...])` sets column names and their order. `writeheader()` writes the header row, followed by `writerows(records)` for the data.

The sequence of writing calls determines the output order. Creating a list earlier only stores records in memory.

Open CSV files with `newline=""` so the CSV module manages line endings. `DictReader` reads fields as text, so convert mark fields before arithmetic.

## JSON: structured data

`json.dump(data, file)` writes JSON, and `json.load(file)` reads it. JSON supports nested dictionaries and lists. CSV is useful for tables with consistent columns.

## Run the file-management example

The illustrative [file_formats.py](../../exercises/session_review/file_formats.py) creates a folder, writes and appends text, reads it back, writes CSV headers and records, and saves/loads JSON. Fictional data and temporary storage make it repeatable.

`python3 exercises/session_review/file_formats.py` prints:

```text
Text: Hello / Hi
CSV columns: name,math,science
CSV rows: 2
JSON rows: 2
```

The temporary folder is removed automatically after the example. For a persistent project, choose a dedicated output directory and be aware that write mode replaces existing contents.

Return to [topics studied](../../PROGRESS.md).
