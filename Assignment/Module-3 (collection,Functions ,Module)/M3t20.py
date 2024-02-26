# Write a Python program to convert a list to a tuple.

def list_to_tuple(input_list):
    # Convert the list to a tuple using the tuple() constructor
    return tuple(input_list)


input_list = [1, 2, 3, 4, 5]
result_tuple = list_to_tuple(input_list)
print("List converted to tuple:", result_tuple)
