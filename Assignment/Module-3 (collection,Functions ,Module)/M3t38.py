# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    
    if not numbers:
        return None, None
    
    return max(numbers), min(numbers)

# Test the function

decimal_numbers = [3.14, 2.718, 1.618, 0.577, 1.732]
maximum, minimum = find_max_min(decimal_numbers)

print("Maximum number:", maximum)
print("Minimum number:", minimum)
