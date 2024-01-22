#write a program  to sum of the first n positive integers.
Number=int(input("Enter a positive integer(n):"))

if Number<=0:
    print("Please Enter positive number.")
else:
    sum=Number*(Number+1)//2

print(f"The sum of positive integers...:{sum}")