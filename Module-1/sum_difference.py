#write a python program that will return  true if the two given integer values are equal or their sum or difference is 5.
Number1=int(input("Enter First Number:"))
Number2=int(input("Enter Second Number:"))

if Number1==Number2 or Number1+Number2==5 or abs(Number1-Number2)==5:
    print("True")
else:
    print("False")