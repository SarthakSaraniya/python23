# Write a Python program to check whether an element exists within a tupal

def element_exists(element, input_tuple):
    
    # Check if the element exists within the tuple
    return element in input_tuple


input_tuple = (1, 2, 3, 4, 5)
element_to_check = int(input("Enter check number : "))

if element_exists(element_to_check, input_tuple):
    print(f"The element {element_to_check} exists in the tuple.")

else:
    print(f"The element {element_to_check} does not exist in the tuple.")
