# Write a Python program to read last n lines of a file. 

def read_last_n_lines(file_path, n):
    try:
            file = open(file_path, 'r') 
            lines = file.readlines()
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line.strip())
                
    except FileNotFoundError:
        print("File not found.")
        
    except Exception as e:
        print("An error occurred:", e)


file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"   
n = int(input("Enter how many line you want to Read : "))
read_last_n_lines(file_path, n)
