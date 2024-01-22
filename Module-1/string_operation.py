#write a python program  to get a single string from two given string  separated by a space and swap the first two characters of each string.
string1=input("Enter first string....")
string2=input("Enter second string.....")

if len(string1)>=2 and len(string2)>=2:
    new_string=string2[:2]+string1[2:]+" "+string1[:2]+string2[2:]
    print(f"string......:{new_string}")
else:
    print("STOP!! string having at least two character....")