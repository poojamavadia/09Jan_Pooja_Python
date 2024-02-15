#Write a Python program to reverse a tuple.
def reverse_tuple(input_tuple):
    return input_tuple[::-1]


my_tuple=(1,2,3,4,5)
reversed_tuple=reverse_tuple(my_tuple)
print("Reversed tuple:",reversed_tuple)
