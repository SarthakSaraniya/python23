# super method

class grandparent() :
    
    def fun(self) :
        super().fun()
        print("This is grandparent")

class parent1 :
    
    def fun(self) :
        super().fun()
        print("This is parent 1 class")
        
class parent2 :
    
    def fun(self) :
        print("This is parent 2 class.")
        
class child(grandparent,parent1,parent2) :
    
    def fun(self) :
        super().fun()
        print("This is a child class.")
        
obj = child()
obj.fun()