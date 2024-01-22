#write a  python function to insert a string in the middle of a string.
def insert_string(b,i):
    middle_index=len(b)//2
    result_string=b[:middle_index]+i+b[middle_index:]
    return result_string

b=input("enter original string......")
i=input("enter string to insert.....")

result=insert_string(b,i)
print(result)
