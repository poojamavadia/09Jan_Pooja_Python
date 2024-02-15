#Write a Python program to convert a tuple to a string.
def tuple_to_string(input_tuple):
    string_tuple = tuple(map(str,input_tuple))
    result_string = ''.join(string_tuple)
    
    return result_string

my_tuple=(1,2,3,4,5)
string_result=tuple_to_string(my_tuple)
print("string:",string_result)
