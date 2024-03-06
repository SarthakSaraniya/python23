file_path = "C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
  # Change this to the path of your file

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read all lines from the file and store them into a list
    lines = file.readlines()

# Now, lines variable contains all the lines from the file
# You can access each line using indexing or iterate over it
for line in lines:
    print(line.strip())  # Print each line (strip() removes trailing newline characters)
