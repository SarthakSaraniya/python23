class Bank :
    
    def openAccount(self,acno,cname,balance) :
        self.acno = acno
        self.cname = cname
        self.balance = balance
        print("Hello",self.cname,"Your Account Number",self.acno,"is open with",self.balance,"Rs.")
        
    def deposit(self,amount) :
        self.balance += amount
        
    def withdraw(self,amount) :
        if amount <= self.balance :
            self.balance -= amount
            
        else :
            print("Sorry you Need Another",amount-self.balance,"Rs.")
            
    def chechBalance (self) :
        print("Your Current balance is : ",self.balance)
        
b1 = Bank()
acno = int(input("Enter Account Number :"))
cname = input("Enter Name of Customer : ")
balance = int(input("Enter intial Balance : ")) 

b1.openAccount(acno,cname,balance)

while True :
    
    print("-"*50)
    manu = """
            1) Deposit
            2) Withdeaw
            3) Check Balance
            4) Exit  
    """
    print(manu) 
    print("-"*50)
    
    choice = int(input("Enter your Choice : "))
    
    if choice == 1 :
        amount = int(input("Enter Deposite Amount : "))
        b1.deposit(amount)
        print("-"*50)
        
    elif choice == 2 :
        amount = int(input("Enter Withdeawal Amount : "))
        b1.withdraw(amount)
        
    elif choice == 3 :
        b1.chechBalance()
        print("-"*50)
        
    elif choice == 4 :
        print("Thank you for using our services.")
        break
    
    else :
        print("Invelid choice. Please Try Again.")
        break
      
   