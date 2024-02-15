#Write a Python program to convert a list of characters into a string.
def list_to_string(characters):
    return ''.join(characters)

char_list=['H','e','l','l','o']
result_string=list_to_string(char_list)
print("Resulting string:",result_string)
