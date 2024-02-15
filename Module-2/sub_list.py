#Write a Python program to check whether a list contains a sub list.
def sublist(main_list, sublist):
    for i in range(len(main_list)):
        if main_list[i:i+len(sublist)]==sublist:
            return True
    return False

main_list=[1,2,3,4,5,6]
sub_list1=[2,3]
sub_list2=[5,6,7]

print("Main list:",main_list)
print("Sublist 1:",sub_list1)
if sublist(main_list,sub_list1):
    print("Sublist 1 is present.")
else:
    print("Sublist 1 is not present.")

print("Sublist 2:",sub_list2)
if sublist(main_list,sub_list2):
    print("Sublist 2 is present.")
else:
    print("Sublist 2 is not present.")
