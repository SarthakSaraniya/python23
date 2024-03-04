try:
    l = [1,2,3,1,2,3]
    choice = int(input("Enter Index : "))
    print(l[choice])
    
except IndexError as e:
    print(e)