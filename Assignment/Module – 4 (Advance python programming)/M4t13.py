# Write a Python program to copy the contents of a file to another file

def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            with open(destination_path, 'w') as destination_file:
                for line in source_file:
                    destination_file.write(line)
        print(f'Contents copied from {source_path} to {destination_path} successfully.')
    except FileNotFoundError:
        print('File not found. Please check the file paths.')
        
source_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
destination_path ="C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module-3 (collection,Functions ,Module)\\Rendom.txt"
copy_file(source_path,destination_path)

