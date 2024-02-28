#  Write a Python program to convert degree to radian

import math

def radian() :
    
    n = int(input("Enter the degree : "))
    radian = n * math.pi / 180
    
    print("Radian of given degree is : ",radian)
    
radian()