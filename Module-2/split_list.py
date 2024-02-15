#Write a Python program to split a list into different variables. 
def split_list(list_to_split):
    var1,var2,var3,var4=list_to_split
    
    return var1,var2,var3,var4

my_list=[1,2,3,4]
var1,var2,var3,var4=split_list(my_list)

print("Variable 1:",var1)
print("Variable 2:",var2)
print("Variable 3:",var3)
print("Variable 4:",var4)
