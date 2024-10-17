import random

numbers = [random.randint(0, 100) for _ in range(20)]

def maximum(arr):
    max_val = arr[0]
    max_i = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_i = i
    return max_val, max_i


print(numbers)
print(maximum(numbers))