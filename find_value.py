def value_count(data, value):
    count = 0
    for row in data:
        for item in row:
            if item == value:
                count += 1
    return count

def value_positions(data, value):
    positions = []
    for r, row in enumerate(data):
        for c, item in enumerate(row):
            if item == value:
                positions.append((r,c))
                
    return positions
            
if __name__ == "__main__":
    value = -1
    data = [[1, 0, -1],
            [-1, -1, 0],
            [0, 1, -1]]
    
    print(value_count(data, value))
    print(value_positions(data, value))
    