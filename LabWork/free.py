class parent():
    def function1(self):
        print("this is grandparent class")

class child1(parent):
    def function2(self):
        print("this is child 1 claas")

class child2(parent):
    def function3(self):
        print("this is child 2 class")

class child3(parent):
    def function3(self):
        print("this is child 3 class") 

class chalid3_1(child3):
    def fun(self) :
        print("Thos is a chlid3 proprtis for chlid 1.")
        
class chlid3_2(child3) :
    def fun1(self) :
        print("Thos is a chlid3 proprtis for chlid 2.")

obj1 = chalid3_1()
obj1.fun()
       
obj = chlid3_2()
obj.fun1()
obj.function1()
obj.function3()
        
