# Login page code with one dict

d ={}

while True :
    Manu = """
        Press 1 for Signup page
        Press 2 for Loging page 
        Press 3 for Exit page
    """
    print(Manu)
    choice = int(input("Enter choice : "))
    
    if choice == 1 :
        print ("<"*25,"Welcome to Signup Page",">"*25)
        name = input("Enter name : ")
        mobile = int(input("Enter mobile number : "))
        password = int(input("Enter password : "))
        cpassword = int(input("Enter confirm  password : "))
        email = input("Enter email : ")
        
        if password == cpassword :
            print("Signup is sucessfull !!")
            d["name"] = name
            d["modile"] = mobile
            d["password"] = password
            d["email"] = email
            
        else :
            print("Password and cpassword not match !!")
            
    elif choice == 2 :
        print ("<"*25,"Welcome to Login Page",">"*25)
        email = input("Enter email : ")
        password = int(input("Enter password : "))
        
        if d["email"] == email and d["password"] == password :
            print("Login Sucessfully !!")
            
        else :
            print("Enter valid email and passwoed .")
            
    elif choice == 3 :
        print("Thank you for using this !!")
        break
    
    else :
        print ("Invelid choice !!")
        break