#Write a Python program to split a list into different variables

def split_list(lst):
    
    # Assuming the list has at least 3 elements
    var1, var2, *remaining = lst
    return var1, var2, remaining

# Example list
my_list = [1,"sarthak",15,10.26,"Dharmik"]

# Split the list into variables
variable1, variable2, remaining_list = split_list(my_list)

print("Variable 1:", variable1)
print("Variable 2:", variable2)
print("Remaining List:", remaining_list)