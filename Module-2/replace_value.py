#Write a Python program to replace last value of tuples in a list.
def replace_last_value(tuples_list,new_value):
    modified_list=[]
    for tup in tuples_list:
        temp_list=list(tup)
        temp_list[-1]=new_value
        modified_list.append(tuple(temp_list))
    return modified_list


tuples_list=[(1,2,3),(4,5,6),(7,8,9)]
new_value=10
modified_list=replace_last_value(tuples_list,new_value)
print("Original list of tuples:",tuples_list)
print("Modified list of tuples:",modified_list)
