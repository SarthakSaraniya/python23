#  Write a Python program to combine two dictionary adding values for comman key 

def combine_dictionaries(d1, d2):
    combined_dict = {}
   
    # Iterate over keys in both dictionaries
    for key in d1.keys() | d2.keys():
       
        # Add values if key exists in both dictionaries
        combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)
    
    return combined_dict


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries
combined_dict = combine_dictionaries(d1, d2)
print("Combined dictionary:", combined_dict)
