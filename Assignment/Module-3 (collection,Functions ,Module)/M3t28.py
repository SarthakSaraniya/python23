#  Write a Python program to create a dictionary from a string.

sample_string = 'w3resource'

# Initialize an empty dictionary to store letter counts
letter_count = {}

# Iterate over each character in the string
for char in sample_string:
    
    # Check if the character is a letter
    if char.isalpha():
       
        # Update the count of the letter in the dictionary
        letter_count[char] = letter_count.get(char, 0) + 1
        
    elif char.isalnum():
        
        # Update the count of the number in the dictionary
        letter_count[char] = letter_count.get(char,0) + 1

print("Dictionary from string:", letter_count)
