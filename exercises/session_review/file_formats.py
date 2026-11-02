"""Illustrative educational example prepared for this repository using fictional data."""

import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory


def demonstrate_formats(folder):
    folder.mkdir(exist_ok=True)
    note_path = folder / "note.txt"
    with note_path.open("w", encoding="utf-8") as file:
        file.write("Hello\n")
    with note_path.open("a", encoding="utf-8") as file:
        file.write("Hi\n")
    with note_path.open("r", encoding="utf-8") as file:
        text = file.read()

    students = [
        {"name": "Alex", "math": 85, "science": 90},
        {"name": "Sam", "math": 70, "science": 80},
    ]
    csv_path = folder / "students.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "math", "science"])
        writer.writeheader()
        writer.writerows(students)
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        csv_rows = list(reader)

    json_path = folder / "students.json"
    with json_path.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)
    with json_path.open("r", encoding="utf-8") as file:
        json_rows = json.load(file)
    return text, columns, csv_rows, json_rows


if __name__ == "__main__":
    with TemporaryDirectory() as temporary_folder:
        text, columns, csv_rows, json_rows = demonstrate_formats(
            Path(temporary_folder) / "practice"
        )
        print("Text:", " / ".join(text.splitlines()))
        print("CSV columns:", ",".join(columns))
        print("CSV rows:", len(csv_rows))
        print("JSON rows:", len(json_rows))
