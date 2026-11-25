#Write write_squares(path, n) that creates the file path (and its parent folder if needed) containing n lines of the form <i> squared is <i*i> for i from 1 to n, and returns n. In the main program write 8 lines to output/squares.txt, print Lines written: 8, then read the file back and print its contents.
from pathlib import Path 

def write_squares(path,n):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        for i in range(1,n+1):
            f.write(f"{i} squared is {i * i}\n")
    return n

output_path = Path("T03_files/squares.txt")
count = write_squares(output_path,8)
print(f"Lines Written: {count}")
print(output_path.read_text(encoding="utf-8"),end="")




