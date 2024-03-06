# Write a Python program to read a file line by line and store it into a list

def line_store_list(file_path) :
    
    try :
        file = open(file_path,'r')
        line = file.readlines()
        print("Contents of the file stored in a list : ",line)
        
    except FileNotFoundError :
        print("File not found")
        
    except Exception as e :
        print("An error occurred:", e)
        
file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
line = line_store_list(file_path)
        