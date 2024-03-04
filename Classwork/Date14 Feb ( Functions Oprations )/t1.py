#function with parameters and with aarguments

def myfun(n) :
    
    fac = 1
    for i in range(1,n+1) :
        fac = fac * i 
        
    print(fac)
    
n = int(input("Enter number : "))
myfun(n)