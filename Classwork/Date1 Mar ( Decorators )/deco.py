def mfx(fx) :
    
    def mmfx() :
        
        print("--- Welcom to this Site ---")
        fx()
        print("--- Thank you for using this Site ---")
        
    return mmfx

@mfx
def fac() :
    
    n = int(input("Enter  the number : "))
    fac= 1
    
    for i in range(1,n+1) :
        fac = fac * i
        
    print("Factorial is : ",fac)
    
fac()
    
@mfx
def add() :
    
    n = int(input("Enter  the number1 : "))
    n1 = int(input("Enter  the number2 : "))
    
    print("Addition of two number is : ",n+n1)
    
add()
    
    