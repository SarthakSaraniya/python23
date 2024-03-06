d = {}

while True :
    
    manu = """
            1) Signup page
            2) Login page 
            3) Exit
        """
        
    print(manu)
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1 :
        print("-"*50,"Welcome to signup page","-"*50)
        name = input("Enter name : ")
        password = int(input("Enter password : "))
        moblie_no = int(input("Enter moblie no : "))
        cpasswoed = int(input("Enter a confrim password :"))
        email = input("Enter email : ")
        
        if password == cpasswoed :
            print("sginup sucessfully !!")
            d['name'] = name
            d['mobile'] = moblie_no
            d['password'] = password
            d['email'] = email
            print(d)
            
        else :
            print("Password And confirm password does not Match!!")
            
    elif choice == 2 :
        print("-"*50,"Welcome to Login page","-"*50 )
        email = input("Enter email : ")
        password = int(input("Enter password : "))
        
        if d['email']== email and d['password'] == password :
            print("Welcome to this game")
            
        else :
            print("Enter valid email and password !!")
            
    elif choice == 3 :
        print("Thank you for using this page.")
        break
    
    else :
        print("invelid choice !!")
        break
    
    
        