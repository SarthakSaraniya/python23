user_input = input("Enter elements separated by spaces: ")

# Split the input string into a list of elements
user_list = user_input.split()

# Using len() function
if len(user_list) == 0:
    print("List is empty")
else:
    print("List is not empty")