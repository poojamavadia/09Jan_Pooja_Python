#Write a Python function that takes two lists and returns true if they have at least one common member. 
def common_member(list1, list2):
    set1=set(list1)
    set2=set(list2)
    
    return bool(set1.intersection(set2))

list1=[1,2,3,4]
list2=[4,5,6,7]

if common_member(list1,list2):
    print("at least one common member.")
else:
    print("Don't have any common member.")
