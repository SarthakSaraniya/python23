class Student :
    
    def getData(self,fname,lname) :
        self.f = fname
        self.l = lname
        
    def putData(self) :
        print("First name : ",self.f)
        print("Last name : ",self.l)
        
s1 = Student()
s1.getData("Sarthak","Saraniya")
s1.putData()