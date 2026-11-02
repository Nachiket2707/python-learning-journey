"""Illustrative educational example prepared for this repository using fictional data."""

even_sum = 0
even_count = 0

for number in range(1, 21):
    if number % 2 == 0:
        even_sum += number
        even_count += 1

print(f"Sum of even numbers: {even_sum}")
print(f"Total even numbers: {even_count}")
