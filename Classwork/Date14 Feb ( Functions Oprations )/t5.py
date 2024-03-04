# function with parameters and with return type

def myfun(a,b):   
    
    return a*b

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

result = myfun(a,b)
print("Multiplication of a*b : ",result)