try:
    n = int(input("Enter Value 1 : "))
    n1 = int(input("Enter Value 2 : "))
    print("Addition : ",n+n1)
    
except ValueError as e:
    print(e)
    
finally:
    print("Thank you!!")