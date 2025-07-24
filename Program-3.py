##  Problem 3: Odd Series Based on Rounding Logic

def custom_odd_series(a: int):
    if a % 2 == 0:
        a -= 1
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    return result

# Example usage:
a = 6
print("Output:", custom_odd_series(a))  
# Output: [1, 3, 5, 7, 9]
