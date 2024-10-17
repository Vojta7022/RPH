import random

def print_data(data):
    for row in data:
        for item in row:
            print(item, end=' ')
        print()
            
def generate_data(n_rows, n_cols):
    arr = [[random.choice((0,1)) for _ in range(n_cols)] for _ in range(n_rows)]
    return arr

arr = generate_data(5, 8)
print_data(arr)
