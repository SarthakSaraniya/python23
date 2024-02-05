str = input("Enter the string : ")
new_str = input("Enter the new string : ")

middle_index = len(str) // 2 

new_str = str[:middle_index] + new_str + str[middle_index:]
print(new_str)