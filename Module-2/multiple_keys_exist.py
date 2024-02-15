#Write a Python program to check multiple keys exists in a dictionary 
def check_multiple_keys(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True

my_dict={'a':1,'b':2,'c':3}

keys_to_check=['a','b','d']
if check_multiple_keys(my_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("key does not exist in the dictionary.")
