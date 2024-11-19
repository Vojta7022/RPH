from pathlib import Path

text = """
Jedna dve, Honza jde, nese pytel mouky.
"""

f = open("text.txt", "wt", encoding="utf-8")
f.write(text)
f.close()

with open("text2.txt", "wt", encoding="utf-8") as f:
    f.write(text)
# Don't have to close the file, it's done automatically

with open("text.txt", "rt", encoding="utf-8") as f:
    text = f.read()
    print(text)

# Path object
path = Path("text.txt")
path.open("rt", encoding="utf-8")
path.write_text(text, encoding="utf-8")

path.read_text(encoding="utf-8")

