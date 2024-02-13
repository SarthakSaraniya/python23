# Given list of strings
strings = ['abca', 'abc', 'xyz', 'xyx', 'radar', 'madam']

# Initialize count variable
count = 0

# Iterate through each string in the list
for string in strings:
    
    # Check if the string length is 2 or more and the first and last characters are the same
    if len(string) >= 2 and string[0] == string[-1]:
        
        # If the conditions are met, increment the count
        count += 1

# Print the count
print("Number of strings where the first and last character are the same:", count)
