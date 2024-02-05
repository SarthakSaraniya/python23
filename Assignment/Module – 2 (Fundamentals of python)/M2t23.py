input_string = input("Enter the string :")

# Check if the length of the string is less than 2

if len(input_string) < 2:
    print("Empty String")
    
# Get the first 2 and last 2 characters of the string

new_string = input_string[:2] + input_string[-2:]
print(new_string)