def myfun():
    n = int(input("Enter number : "))
    c = 0 
    
    for i in range(1,n+1) :
        if n%i == 0 :
            c += 1
            
    if c == 2 :
        print(n,"is prime number.")
        
    else :
        print(n,"is not prime number.")
        
def fac() :
    n = int(input("Enter number : "))
    fac = 1 
    
    for i in range(1,n+1):
        fac = fac*i
        
    print("Factorial is : ",fac)
    
    
myfun()
print("*"*50)
fac()