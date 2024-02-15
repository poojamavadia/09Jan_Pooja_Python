#Write a Python program to remove duplicates from a list.
def remove_duplicates(input_list):
    return list(set(input_list))


original_list=[1,2,3,4,2,3,5]
unique_list=remove_duplicates(original_list)
print("Original list:", original_list)
print("List after removing duplicates:", unique_list)
