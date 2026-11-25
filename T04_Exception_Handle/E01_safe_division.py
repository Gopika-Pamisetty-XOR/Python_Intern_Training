

import sys


def divide_line(line):
    try:
        a_text, b_text = line.split()
        a = float(a_text)
        b = float(b_text)
        result = a / b
    except ValueError:
        return "Invalid input: expected two numbers"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return f"{a:g} / {b:g} = {result:g}"


# for line in sys.stdin:
#     if line.strip() == "":
#         continue
#     print(divide_line(line))



results = []

for line in sys.stdin:
    if line.strip() == "":
        continue
    results.append(divide_line(line))

for res in results:
    print(res)
