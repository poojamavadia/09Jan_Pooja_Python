#Write a Python program to get unique values from a list 
def unique_values(input_list):
    return list(set(input_list))


original_list=[1, 2, 2, 3, 4, 4, 5]
unique_values=unique_values(original_list)
print("Original list:",original_list)
print("List with unique values:",unique_values)
