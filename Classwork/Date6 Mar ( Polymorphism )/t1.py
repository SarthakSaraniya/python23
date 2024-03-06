# super mathod  

class parent :
    
    def fun(self) :
        print("This is a parent class.")
        
    def fun1(self) :
        print("This is 2 method of parent class.")
        
class child(parent) :
    
    def fun(self) :
        super().fun()
        print("This is a child class.")
        
obj = child()
obj.fun()
obj.fun1()