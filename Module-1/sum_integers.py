#write a python program to sum of three given integers.however two values are equal sum will be zero.

Num1=int(input("Enter the first integer: "))
Num2=int(input("Enter the second integer: "))
Num3=int(input("Enter the third integer: "))

if Num1==Num2 or Num1==Num3 or Num2==Num3:
    result = 0
else:
    result = Num1 + Num2 + Num3

print(f"The sum is: {result}")
