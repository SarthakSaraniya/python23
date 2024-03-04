# rendom module 

import random 

r = random.randint(1,50)

print(">"*30,"Welcom to the Game ","<"*30)
print(">"*30,"Guess number between range 1 to 50 ","<"*30)

status = True

while status :
    
    choice = int(input("Enter choice :"))
    
    if choice < r :
        print("Plese gusee gretest number .")
        
    elif choice > r :
        print("Plese gusee smaller number .")
        
    elif choice == r :
        print("You win !!")
        status = False
        
    else :
        print("Invelid choice !!")
        status = False