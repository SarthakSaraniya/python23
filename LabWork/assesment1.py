d = {}   
while True :
    
    print("-"*25," WELCOME TO FRUIT MARKET ","-"*25)
    
    manu = """
                1) Manager
                2) Customer    
    """
    
    print(manu)
    
    role = int(input("Select your Role : "))
    
    if role == 1 :
        while True :
        
            manu = """
                        --- Fruit Market Manager ---
                        1) Add Fruit stock
                        2) View Fruit stock
                        3) Updet Fruit stock 
                        4) Exit       
                """
            print(manu)
            choice = int(input("Enter your choice : "))
        
            if choice == 1 :
            
                print("--- ADD FRUIT STOCK --- ")
                n = int(input("How many Fruit you want to add : "))
            
                for i in range(n):
                    name = input(("Enter fruit Name : "))
                    quantity = int(input(("Enter qty (in Kg) : ")))
                    price = int(input(("Enter price : ")))
                    d[name] = {'qty' : quantity , 'price' : price}
                    
                print("Add Fruit : ",d)                    
                s = input("Do you want to perfom more operations : press y for yes and n for no : ")       
              
        
            elif choice == 2 :
                print("--- VIEW FRUIT STOCK ---")
                print("Current Fruit Stock is : ",d)
                
            elif choice == 3 :
                print("--- UPDATE FRUIT STOCK ---")
                print("Current Stock is : ",d)
                n = int(input("Enatr the you want to add new Fruit :"))
                
                for i in range(n) :
                
                    new_name = input("Enter the Fruit name : ")
                    new_quantity = int(input("Enter qty (in Kg) : "))
                    new_price = int(input("Enter price : "))                
                    d[new_name] = {'qty' : new_quantity , 'price' : new_price}
                    
                print("Update Fruit Stock is : ",d)
                
            elif choice == 4 :
                print("--- Thank you for survice ---")
                break
            
    elif role == 2 :
        print("--- Welcome Customer ---")
        break
            