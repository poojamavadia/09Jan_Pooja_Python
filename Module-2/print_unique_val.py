#Write a Python program to print all unique values in a dictionary.
def unique_values(dictionary):
    unique_vals = set()
    for value in dictionary.values():
        unique_vals.add(value)
    return unique_vals


my_dict={'a':100,'b':200,'c':100,'d':300,'e':200}
unique_vals=unique_values(my_dict)
print("Unique values in the dictionary:",unique_vals)
