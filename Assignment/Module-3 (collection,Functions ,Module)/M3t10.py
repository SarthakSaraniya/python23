#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_ele(list1):
    l1=set(list1)
    l2=list(l1)
    return l2

ori_list=[1,2,3,3,4,5,5,6,2,5]
print(unique_ele(ori_list))