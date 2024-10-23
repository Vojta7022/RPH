import random

def print_data(data):
    for row in data:
        for item in row:
            print(item, end=' ')
        print()
            
def generate_data(n_rows, n_cols):
    return [[random.choice((0,1)) for _ in range(n_cols)] for _ in range(n_rows)]
    

def line_size(r, c, data):
    count = 1
    i = c-1
    while i >= 0 and data[r][i] == data[r][c]:
        count += 1
        i -= 1
        
    i = c+1
    while i < len(data[r]) and data[r][i] == data[r][c]:
        count += 1
        i += 1
            
    return count

def line_size_all_directions(r, c, data, direction):
    count = 1
    dr, dc = direction
    
    i = r - dr
    j = c - dc
    while 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i][j] == data[r][c]:
        count += 1
        i -= dr
        j -= dc
        
    i = r + dr
    j = c + dc
    while 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i][j] == data[r][c]:
        count += 1
        i += dr
        j += dc
            
    return count

arr = generate_data(10, 10)
print_data(arr)
print()
print(line_size(2, 3, arr))
print(line_size_all_directions(2, 3, arr, (1, 1)))
