#write a python program to test whether a passesletter is a vowel or not.
# Get user input for a letter
Letter=input("Enter a letter: ")
Letter=Letter.lower()
if Letter in 'aeiou':
    print(f"{Letter} is a vowel.")
else:
    print(f"{Letter} is not a vowel.")
