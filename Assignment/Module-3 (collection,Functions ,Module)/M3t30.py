#  Write a Python function to check whether a number is in a given range .

def in_range():
    
    start = int(input("Enatr the start value : "))
    end = int(input("Enter the end value : "))
    
    n = int(input("Enter the number is check : "))
    
    if start < end :
        
        if n > start and n < end :
            print(n,"Number is in the given range. ")
            
        elif n < start or n > end :
            print(n,"Number is not in range !")
            
    else :
            print("Enter the valid range !!")
            
in_range()