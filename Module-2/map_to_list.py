#Write a Python program to map two lists into a dictionary
def lists_to_dict(keys,values):
    return {key: value for key, value in zip(keys, values)}


keys=['a','b','c']
values=[1,2,3]

result_dict=lists_to_dict(keys,values)
print("Mapped dictionary:",result_dict)
