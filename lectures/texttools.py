def count_rows_and_words(filename):
    with open(filename, "rt", encoding="utf-8") as f:
        text = f.read()
        lines = text.split("\n")
        words = []
        for line in lines:
            words += line.split()
            
    return (len(lines), len(words))

def compute_word_frequencies(filename):
    with open(filename, "rt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        frequencies = {}
        for word in words:
            word = word.lower()
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
                
    return frequencies

if __name__ == "__main__":
    print(compute_word_frequencies("text.txt"))
            
