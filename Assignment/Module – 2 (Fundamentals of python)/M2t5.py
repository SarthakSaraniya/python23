# Swapping two numbers with a temporary variable using if-else
def swap_with_temp_if_else(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage
num1 = int(input("Enter the 1st number :"))
num2 = int(input("Enter the 2st number :"))

# Swapping with temp variable using if-else
num1, num2 = swap_with_temp_if_else(num1, num2)
print("After swapping with temp variable using if-else:", num1, num2)

# Swapping two numbers without a temporary variable using if-else
def swap_without_temp_if_else(a, b):
    if a != b:
        a = a + b
        b = a - b
        a = a - b
    return a, b

# Resetting values for swapping without temp variable using if-else
num1 = 5
num2 = 10

# Swapping without temp variable using if-else
num1, num2 = swap_without_temp_if_else(num1, num2)
print("After swapping without temp variable using if-else:", num1, num2)
