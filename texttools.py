def count_rows_and_words(filename):
    with open(filename, "rt", encoding="utf-8") as f:
        text = f.read()
        lines = text.split("\n")
        words = []
        for line in lines:
            words += line.split()
            
    return (len(lines), len(words))

if __name__ == "__main__":
    print(count_rows_and_words("text.txt"))
            
