#  Write a Python function to calculate the factorial of a number (no nagetive integer)

def factorial() :
    
    n = int(input("Enter the number : "))
    fac = 1
    
    for i in range(1,n+1) :
        
        fac = fac * i 
        
    print("factorial is : ",fac)
    
factorial()