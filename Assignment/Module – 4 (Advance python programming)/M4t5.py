# Write a Python program to append text to a file and display the text

class file() :
    def append_text_to_file(self,file_path, text_to_append):
        try:
                file =  open(file_path, 'a') 
                file.write(text_to_append)
                print("Text appended to the file successfully.")
            
        except FileNotFoundError:
            print("File not found.")
        
        except Exception as e:
            print("An error occurred:", e)

    def display_file_contents(self,file_path):
        try:
                file = open(file_path, 'r') 
                file_contents = file.read()
                print("File contents:")
                print(file_contents)
            
        except FileNotFoundError:
            print("File not found.")
        
        except Exception as e:
            print("An error occurred:", e)


file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
text_to_append = "\nThis is the appended text."
f = file()
f.append_text_to_file(file_path, text_to_append)
f.display_file_contents(file_path)
