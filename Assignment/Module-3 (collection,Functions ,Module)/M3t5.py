my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
dup_list = []

# looping for chack duplicate vaule in my_list
for i in my_list :
    
    # enter the duplicate vaule in dup_list
    if i not in dup_list :
        dup_list.append(i)
        
# print dup_list
print(dup_list)