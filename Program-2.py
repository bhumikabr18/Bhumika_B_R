## Problem 2: Series – Odd Numbers Until a Elements

def odd_series(a: int):
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    return result

# Example usage:
a = 4
print("Output:", odd_series(a))  
# Output: [1, 3, 5, 7]
