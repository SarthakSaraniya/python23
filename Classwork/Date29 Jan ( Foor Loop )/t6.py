# Initialize the total sum
total_sum = 0

# Iterate through the range from 100 to 199
for number in range(100, 200):
    # Convert the number to a string to easily access each digit
    digits = str(number)
    
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in digits)
    
    # Check if the sum of the digits is odd
    if digit_sum % 2 != 0:
        # Add the number to the total sum
        total_sum += number

# Print the result
print(f"The sum of all three-digit numbers in the range (100, 200) where the sum of the digits is odd is: {total_sum}")
