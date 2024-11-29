def read_classification_from_file(filepath):
    classifications = {}
    with open(filepath, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split()
            classifications[key] = value
            
    return classifications
            
if __name__ == '__main__':
    classifications = read_classification_from_file('!truth.txt')
    print(classifications)
