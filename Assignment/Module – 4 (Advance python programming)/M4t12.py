# Write a Python program to write a list to a file. 

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')
            
file_path ="C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
data_list = ['apple', 'banana', 'cherry', 'date']
write_list_to_file(file_path,data_list)

print("The list has been written to : ",file_path)