#Write a Python program to returns sum of all divisors of a number
def divisors(number):
    divisor_sum = 0
    for i in range(1,number+1):
        if number % i==0:
            divisor_sum+=i
    return divisor_sum


number=12
divisor_sum=divisors(number)
print("Sum of all divisors of",number,"is:",divisor_sum)
