## Problem 4: Count of Multiples from List for 1 to 9

def count_multiples(numbers: list):
    result = {}
    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

# Example usage:
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print("Output:", count_multiples(nums))
# Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
