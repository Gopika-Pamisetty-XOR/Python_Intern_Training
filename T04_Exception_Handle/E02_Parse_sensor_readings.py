#data/readings.txt holds temperature readings, one per line, but some lines are not numbers. Write parse_readings(lines) that returns (values, bad): values is a list of floats, bad is a list of (line_number, text) for lines that cannot be converted (line numbers start at 1; text is stripped). Print: the number of lines, the number of valid readings, the list of invalid line numbers, each invalid line as line <n>: <text as repr>, the average with two decimals, and the minimum and maximum

from pathlib import Path


def parse_readings(lines):
    values = []
    bad = []

    for line_num, raw_line in enumerate(lines, start=1):
        text = raw_line.strip()
        try:
            num = float(text)
            values.append(num)
        except ValueError:
            bad.append((line_num, text))

    return values, bad


lines = Path("T04_Exception_Handle/readings.txt").read_text(encoding="utf-8").splitlines()
values, bad = parse_readings(lines)

print(f"Lines: {len(lines)}")
print(f"Valid: {len(values)}")
print(f"Invalid lines: {[line_num for line_num, _ in bad]}")

for line_num, text in bad:
    print(f"  line {line_num}: {text!r}")

if values:
    print(f"Average: {sum(values) / len(values):.2f}")
    print(f"Min: {min(values)}  Max: {max(values)}")
