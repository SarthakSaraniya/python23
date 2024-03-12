# Magic Method & Opreter Overloding

class point :
    def __init__(self,x,y) :
        print("Init called .")
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        print(" Str called . ")
        return "({0},{1})".format(self.x,self.y)
    
    def __sub__(self,obj) :
        print("Subtrection called.")
        x = self.x - obj.x
        y = self.y - obj.y
        return point(x,y)
    
p1 = point(50,60)
print(p1)
p2 = point(30,40)
print(p2)
print("Subtrection of Object : ",p1-p2)