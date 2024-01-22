def my_function(input_str):
    not_index=input_str.find('not')
    poor_index=input_str.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        input_str=input_str[:not_index]+'good'+input_str[poor_index+4:]
    return input_str

s="The weather is not poor today.I hope it gets better tomorrow."
result=my_function(s)
print(result)
