#write a python program to get a string made of the first 2 and the last char from a given a string.If the string length is less than 2,return instand of the empty string.
def my_function(input_str):
    if len(input_str)>=2:
        result_str=input_str[:2]+input_str[-1]
    else:
        result_str=""

    return result_str

s="python"
result=my_function(s)
print(result)
