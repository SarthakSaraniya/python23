# Write a Python program to count the number of lines in a text file.

def line_count(file_path) :
    
    try :
        file = open(file_path,'r')
        line_counts = sum(1 for line in file)
        return line_counts
    
    except FileNotFoundError :
        print(f"Error: File '{file_path}' not found.")
        return []
    
file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
line_counts = line_count(file_path)
print("Number of lines in file is : ",line_counts)
        