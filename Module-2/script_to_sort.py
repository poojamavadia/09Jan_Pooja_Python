#Write a Python script to sort (ascending and descending) a dictionary by value. 
my_dict={'a':4,'b':2,'c':7,'d':1}

sorted_ascending=dict(sorted(my_dict.items(),key=lambda x: x[1]))
sorted_descending = dict(sorted(my_dict.items(),key=lambda x:x[1],reverse=True))

# Print the sorted dictionaries
print("ascending order:",sorted_ascending)
print("descending order:",sorted_descending)
