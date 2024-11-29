import random

def print_data(data):
    for row in data:
        for item in row:
            print(item, end=' ')
        print()
        
def format_data(data):
    return '\n'.join([' '.join(map(str, row)) for row in data])
            
def generate_data(n_rows, n_cols):
    return [[random.choice((0,1)) for _ in range(n_cols)] for _ in range(n_rows)]
    

def line_size(r, c, data):
    directions = [(0,1),(0,-1)]
    return sum(line_size_any_direction(r, c, data, d) for d in directions) + 1

def line_column_size(r, c, data):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    return sum(line_size_any_direction(r, c, data, d) for d in directions) + 1

def region_size(r, c, data):
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
    return sum(line_size_any_direction(r, c, data, d) for d in directions) + 1

def line_size_any_direction(r, c, data, direction):
    count = 1
    dr, dc = direction
    
    i = r + dr
    j = c + dc
    while 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i][j] == data[r][c]:
        count += 1
        i -= dr
        j -= dc
            
    return count

arr = generate_data(10, 10)
print_data(arr)
print()
print(line_size(2, 3, arr))
print(region_size(2, 3, arr))

