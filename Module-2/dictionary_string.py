#Write a Python program to create a dictionary from a string. 
def dict(input_string):
    char_count_dict={}
    for char in input_string:
        if char in char_count_dict:
            char_count_dict[char]+=1
        else:
            char_count_dict[char]=1
    return char_count_dict


input_string='source'
result_dict=dict(input_string)
print("Dictionary from string:",result_dict)
