# Write a Python program to read an entire text file

def read_text_file(file_path) :
    
    try :
        file = open(file_path,"r")
        print(file.readline())
        file.close
        
    except FileNotFoundError :
        print("File not Found !!")
        
    except Exception as e:
        print("An error occurred:", e)
        

file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
red = read_text_file(file_path)