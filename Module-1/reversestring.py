#write a python function to reverse a string if its length is a multiple of 4.
def reverse_string(i):
    if len(i)%4==0:
        r=i[::-1]
        return r
    else:
        return i
    
i=input("Enter a string....")
result=reverse_string(i)
print(result)