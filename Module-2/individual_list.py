#Write a Python program to unzip a list of tuples into individual lists.
def unzip_list_of_tuples(list_of_tuples):
    unzipped_lists = zip(*list_of_tuples)
    
    individual_lists = [list(lst) for lst in unzipped_lists]
    
    return individual_lists

list_of_tuples=[(1,4,7),(2,5,8),(3,6,9)]
unzipped_lists=unzip_list_of_tuples(list_of_tuples)
print("Unzipped lists:")
for lst in unzipped_lists:
    print(lst)
