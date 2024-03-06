# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        area = self.length * self.width
        print("Rectangle Area is : ",area)       


length = int(input("Enter Rectabgle Length is : "))
width = int(input("Enter Rectangle Width is : "))
rectangle = Rectangle(length,width)
rectangle.compute_area()


