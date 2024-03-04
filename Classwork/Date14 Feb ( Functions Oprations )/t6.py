from main import*

while True :
    
    manu = """
                prass 1 for string Reverse
                prass 2 For Count length of string
                prass 3 for string in uppercase
                prass 4 exit    
    
    """
    print(manu)
    print("<"*25,">"*25)
    
    choice = int(input("Enter choice : "))
    
    if choice == 1 :
        srevers()
        
    elif choice == 2 :
        length()
        
    elif choice == 3 :
        upper()
        
    elif choice == 4 :
        print("Thank you for Using this app !!")
        break
    
    else:
        print("Invelid choice !!")
        break
    
        
    