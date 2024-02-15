#Write a Python program to remove an empty tuple(s) from a list of tuples.
def remove_empty_tuples(tuple_list):
    non_empty_tuples=[tup for tup in tuple_list if tup]
    return non_empty_tuples


list_of_tuples=[(1, 2, 3),(),(4, 5),(),(),(6,),()]
filtered_list=remove_empty_tuples(list_of_tuples)
print("Original list of tuples:",list_of_tuples)
print("List of tuples after removing empty tuples:",filtered_list)
