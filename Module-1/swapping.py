#write a python program for Swapping
Number_one=int(input("Enter First Number:"))
Number_Two=int(input("Enter Second Number:"))

print(f"Before Swapping Number is:\nFirst Number:{Number_one}\nSecond Number:{Number_Two}")

print("Swapping done with temparary variables....")

temp=Number_one
Number_one=Number_Two
Number_Two=temp

print(f"After Swapping Number is:\nFirst Number:{Number_one}\nSecond Number:{Number_Two}")

Number_one=int(input("Enter First Number:"))
Number_Two=int(input("Enter Second Number:"))

print("Swapping done without temparary variables.....")

Number_one=Number_one+Number_Two
Number_Two=Number_one-Number_Two
Number_one=Number_one-Number_Two

print(f"After Swapping Number is:\nFirst Number:{Number_one},\nSecond Number:{Number_Two}")
