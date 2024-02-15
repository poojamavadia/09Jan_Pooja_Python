#Write a Python program to convert a list to a tuple.
def list_to_tuple(input_list):
    return tuple(input_list)


my_list=[1,2,3,4,5]
converted_tuple=list_to_tuple(my_list)
print("Converted tuple:",converted_tuple)
