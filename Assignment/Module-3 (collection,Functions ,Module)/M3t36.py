# Write a Python program to calculate surface volume and area of a cylinder

import math 

def cylinder_surface(radius,height):
    
    surface = 2 * math.pi * radius * (radius + height)
    print("Cylinder surface is : ",surface)
    
def cylinder_area(radius,height) :
    
    area = math.pi * radius ** 2 * height
    print("Cylinder area is : ",area)
    
radius = int(input("Enter the cylinder radius : "))
height = int(input("Enter the cylinder height : "))
cylinder_surface(radius,height)
cylinder_area(radius,height)
