#Write a Python program to find the highest 3 values in a dictionary 
def highest(dictionary,n=3):
    sorted_items=sorted(dictionary.items(),key=lambda x: x[1],reverse=True)
    return sorted_items[:n]

my_dict={'a':10,'b':20,'c':30,'d':40,'e':50}

highest_values=highest(my_dict)
print("Highest 3 values:",highest_values)
