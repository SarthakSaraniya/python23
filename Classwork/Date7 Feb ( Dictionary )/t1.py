d = {1:"sarthak",2:"Ary",3:"sahil",4:"Dharmik"}
print(d)

print(d.items()) # print all value in tupal
print(d.keys())  # print all key no in list

d.update({10:"Tithi",15:"Manshi"})  # input multipal value
print(d)

d.popitem()  # pop last key and value
print(d)

d.pop(2)  # pop given key value 
print(d)

t = (1,2,"sarthak")
d1 = dict.fromkeys(t)   # convert tupal value in dic key value  
print(d1)

d1.setdefault("Ary")
print(d1)