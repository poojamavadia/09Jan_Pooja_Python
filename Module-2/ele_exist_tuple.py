#Write a Python program to check whether an element exists within a tuple.
def check_element_in_tuple(input_tuple, element):
    return element in input_tuple

my_tuple=(1,2,3,4,5)
element_to_check=3

if check_element_in_tuple(my_tuple,element_to_check):
    print(f"The element {element_to_check} exists in the tuple.")
else:
    print(f"The element {element_to_check} does not exist in the tuple.")
 