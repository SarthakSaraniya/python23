# Example dictionary
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

# Initialize variables to store the highest 3 values
highest_values = [float('-inf')] * 3

# Iterate over the dictionary
for value in my_dict.values():
    
    if value > highest_values[0]:
        highest_values = [value, highest_values[0], highest_values[1]]
    
    elif value > highest_values[1]:
        highest_values = [highest_values[0], value, highest_values[1]]
    
    elif value > highest_values[2]:
        highest_values[2] = value

# Display the highest 3 values
print("Highest 3 values in the dictionary:", highest_values)
