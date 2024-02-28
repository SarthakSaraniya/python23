#  Write a Python program to combine values in python list of dictionaries.

sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_values = {}

for data in sample_data:
    
    item = data['item']
    amount = data['amount']
   
    if item in combined_values:
        combined_values[item] += amount
    
    else:
        combined_values[item] = amount

print("Combined values:", combined_values)
