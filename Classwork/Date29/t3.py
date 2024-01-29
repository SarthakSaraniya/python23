n = int(input("Enter the number :"))

ev = 0
od = 0
evcount = 0
odcount = 0

for i in range(1,n+1):
     if i%2==0:
        print(i,"Even number.")
        ev += 1
        evcount += i
        
     else :
        print(i,"Odd number.") 
        od += 1
        odcount += i
     
     
print("Even number are :",ev)
print("Odd number are :",od)
print("Sum of Even number are :",evcount)
print("Sum of Odd number are :",odcount)