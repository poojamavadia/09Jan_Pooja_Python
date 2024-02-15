#Write a Python function to check whether a number is perfect or not. 
def is_perfect_number(number):
    if number<=0:
        return False

    divisor_sum=0
    for i in range(1,number):
        if number % i==0:
            divisor_sum+=i

    return divisor_sum==number

number_to_check=28
if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number")
else:
    print(f"{number_to_check} is not a perfect number")
