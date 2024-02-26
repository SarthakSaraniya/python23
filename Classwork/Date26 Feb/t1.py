class myclass :
    
    def myfun1(self):
        n = input("Enter the string : ")
        s1 = n[::-1]
        print("Revers the string : ",s1)
        
    def myfun2(self):
        l = [1,2,3,4]
        l1 = [6,5,7,8]
        d = {}
        
        if len(l) == len(l1) :
            for i in l :
                for j in l1 :
                    d[i] = j
                    l1.remove(j)
                    break
        print(d)
        
    def myfun3(self) :
        print("This is a function 3 !!")
        
obj = myclass()
obj.myfun1()
obj.myfun2()
obj.myfun3()
        
        