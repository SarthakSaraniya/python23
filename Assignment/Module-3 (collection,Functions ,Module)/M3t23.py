# Write a Python program to convert a list of tuples into a dictionary

def list_of_tuples_to_dict(tuple_list):
    
    # Convert list of tuples to dictionary using dictionary comprehension
    result_dict = {key: value for key, value in tuple_list}
    return result_dict


tuple_list = [('a', 1), ('b', 2), ('c', 3)]
result_dict = list_of_tuples_to_dict(tuple_list)
print("Dictionary:", result_dict)
