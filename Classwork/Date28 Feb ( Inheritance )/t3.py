# Multiple Inheritance

class grendparent :
    
    def fac(self):
        
        print("--- Factorial ---")
        n = int(input("Enter the number : "))
        fac = 1 
        
        for i in range(1,n+1) :
            fac = fac * i
            
        print("Factorial is : ",fac)
        
class parent :
    
    def list(self) :
        
        print("--- Revers List ---")
        my_list = [1, 2, 3, 4, 5]
        my_list.reverse()
        print(my_list)
        
    def middle_string(self) :
        
        print("--- Middle value in String ---")
        s = input("Enter the string : ")
        
        middle_index = len(s) // 2
        
        if len(s) % 2 == 1 :
            middle_string = s[middle_index]
            print("Middle value : ",middle_string)
            
        else :
            middle_strings = [s[middle_index - 1], s[middle_index]]
            print("Middle value is : ",middle_strings)
            
class child(grendparent,parent) :
    
    def prime(self) :
        
        print("--- Prime Number ---")
        n = int(input("Enter the number : "))
        
        if n > 1:        
            for i in range(2, n):                
                if (n % i) == 0:                    
                    print(n, "is not a prime number")
                    break
                   
                else:
                    print(n, "is a prime number")
                    break
    
        else:
             print(n, "Enter velid number !!")
             
obj = child()
obj.fac()
obj.list()
obj.middle_string()
obj.prime()