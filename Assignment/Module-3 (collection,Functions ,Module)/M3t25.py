#  Write a Python program to print all unique values in a dictionary

# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Initialize a set to store unique values
unique_values = set()

# Iterate over the values in the dictionary
for value in my_dict.values():
    unique_values.add(value)

# Print the unique values
print("Unique values in the dictionary:", unique_values)
