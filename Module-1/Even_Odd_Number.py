#write a python program whether a given number is even or odd and print out an appropriate message to the user.

Number=int(input("Enter a number: "))

if Number % 2 == 0:
    print(f"{Number} is an even number.")
else:
    print(f"{Number} is an odd number.")
