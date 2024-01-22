#write a python program to count  occurances of a substring in a string.
main_string=input("Enter the main string...:")
substring=input("Enter substring to be count:")

count=0

for i in range(len(main_string)-len(substring)+1):
    if main_string[i:i+len(substring)]==substring:
        count+=1

print(f"The number of occurances of a given string is..:{count}")