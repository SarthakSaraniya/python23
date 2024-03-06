# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle :
    
    def __init__(self,redius) :
        self.redius = redius
        
    def area(self) :
        area =math.pi * self.redius ** 2
        print("Circle Area is : ",area)
        
    def perimeter(self) :
        pera = 2 * math.pi * self.redius
        print("Circle Perimeter is : ",pera)
        
redius = int(input("Enter Circle redius : "))
circle = Circle(redius)
circle.area()
circle.perimeter()   
