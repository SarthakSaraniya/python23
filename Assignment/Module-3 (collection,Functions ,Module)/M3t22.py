def replace_last_value(list , new_value):
    
    # Iterate over the list of tuples and replace the last value of each tuple
    new_list = [(*t[:-1], new_value) for t in list]
    return new_list

list  = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_value = int(input("Enter the replace value : "))

new_list = replace_last_value(list , new_value)
print("Updated list of tuples:", new_list)
