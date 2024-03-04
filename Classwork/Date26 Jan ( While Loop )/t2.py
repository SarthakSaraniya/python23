n = int(input("Enter the number :"))
i = 1
ev = 0
od = 0
evcount = 0
odcount = 0

while (i<=n):  
    if i%2==0:
        print(i,"Even number.")
        ev += 1
        evcount += i
        
    else :
        print(i,"Odd number.") 
        od += 1
        odcount += i
    
    i += 1
    
print("Even number are :",ev)
print("Odd number are :",od)
print("Sum of Even number are :",evcount)
print("Sum of Odd number are :",odcount)