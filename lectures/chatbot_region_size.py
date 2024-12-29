def region_size(r, c, data):
    value = data[r][c]
    count = 1  # Start with the initial position

    # Define directions: horizontal, vertical, and diagonal
    directions = [
        (0, 1), (0, -1),  # Horizontal
        (1, 0), (-1, 0),  # Vertical
        (1, 1), (-1, -1),  # Diagonal
        (1, -1), (-1, 1)  # Anti-diagonal
    ]

    for dr, dc in directions:
        i, j = r + dr, c + dc
        while 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i][j] == value:
            count += 1
            i += dr
            j += dc

    return count

# Příklad použití
data = [
    [1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0]
]
reg_size = region_size(2, 6, data)
print(reg_size)  # Output: 12
