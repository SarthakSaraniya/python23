#function with parameters and with aarguments

def myfun(n) :
    c = 0
    for i in range(1,n+1) :
        if n%i == 0 :
            c += 1
            
    if c == 2 :
        print("prime number :",n)
        
    else :
        print(n,"is not prime number.")
        

n = int(input("Enter number :"))
myfun(n)            
    