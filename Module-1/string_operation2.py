#write  python program to add 'ing' at the end of a given string(length would be at least 3).If given string is already ends with 'ing' then add 'ly' instand string length of the given string is less than 3,leave it unchanged.
def my_function(input_str):
    if len(input_str)>=3:
        if input_str[-3:]=='ing':
            input_str+='ly'
        else:
            input_str+='ing'

    return input_str

s="read"
result=my_function(s)
print(result)
