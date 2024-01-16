#write a python program to get the Fibonacci Series of given range.
Range_Length=int(input("Enter range for Fibonacci Series...:"))
if Range_Length<=0:
    print("Please enter positive range.")
else:
    Fib_series=[]
    a,b=0,1

    for _ in range(Range_Length):
        Fib_series.append(a)
        a,b=b,a+b
    
    print(f"Fibonacci series is:{Fib_series}")