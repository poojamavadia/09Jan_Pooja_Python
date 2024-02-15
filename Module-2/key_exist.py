#Write a Python script to check if a given key already exists in a dictionary.
def key_exists(dictionary, key):
    return key in dictionary


my_dict={'a':1,'b':2,'c':3}

key_to_check='b'
if key_exists(my_dict,key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
