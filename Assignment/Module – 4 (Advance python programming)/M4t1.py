# Write python program that user to enter only odd numbers, else will raise an exception.

def odd_num() :
    while True :
        try :
            num = int(input("Enter the number : "))
            
            if num %2 != 0 :
                return num 
            
            else :
               raise ValueError ("Even number enter")
           
        except ValueError :
            print("Please enter odd number.")
            
resut = odd_num()
print("You entered:", resut)
                
                
            
 