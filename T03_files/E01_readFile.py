#Open data/notes.txt with a with statement and encoding="utf-8". Print the first 5 lines, each preceded by its line number (right-aligned in width 3, then a colon and a space). Then write file_stats(path) that returns a dictionary with lines, words, characters (not counting the line ending) and blank (lines that are empty or only spaces), and print the four values.

def file_stats(path):
    lines = 0
    words = 0
    characters = 0
    blank = 0
    with open(path, encoding="utf-8") as file:
        for line in file:
            clean_line = line.rstrip("\r\n")
            lines+=1
            words+=len(clean_line.split())
            characters+= len(clean_line)
            if clean_line.strip() == "":
                blank+=1
    return {
        "lines": lines,
        "words": words,
        "characters": characters,
        "blank": blank
    }
    
path = "T03_files/notes.txt"

with open(path, encoding="utf-8") as file:
    for line_num, line in enumerate(file, start = 1):
        if line_num>5:
            break
        clean_line = line.rstrip("\r\n")
        if clean_line == "":
            print(f"{line_num:3d}:")
        else:
            print(f"{line_num:3d}: {clean_line}")


stats = file_stats(path)

print(f"Lines: {stats["lines"]}")
print(f"Words: {stats["words"]}")
print(f"Characters: {stats["characters"]}")
print(f"Blank lines: {stats["blank"]}")

