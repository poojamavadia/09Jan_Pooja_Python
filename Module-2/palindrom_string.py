#Write a Python function that checks whether a passed string is palindrome or not
def palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

input_string="A man,a plan,a canal,Panama"
if palindrome(input_string):
    print(f"'{input_string}' is a palindrome")
else:
    print(f"'{input_string}' is not a palindrome")
