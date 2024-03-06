# Write a Python program to read first n lines of a file

def read_first_n_lines(file_path, n):
    try:
            file = open(file_path, 'r') 
            lines = file.readlines()
            for i in range(min(n, len(lines))):
                print(lines[i].strip())
                
    except FileNotFoundError:
        print("File not found.")
        
    except Exception as e:
        print("An error occurred:", e)


file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt" 
n = int(input("How many lines user want to read : "))  
read_first_n_lines(file_path, n)
