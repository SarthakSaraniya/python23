# Write a Python program to calculate the area of a trapezoid

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

# Test the function
base1 = int(input("Enter the base1 value : "))
base2 = int(input("Enter the base2 value : "))
height = int(input("Enter the height value : "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is {area}.")
