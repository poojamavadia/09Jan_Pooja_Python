#Write a Python function to check whether a number is in a given range
def in_range(number,start,end):
    return start<=number<= end

number_to_check=5
start_range=1
end_range=10

if in_range(number_to_check,start_range,end_range):
    print(f"{number_to_check} is in the range [{start_range},{end_range}]")
else:
    print(f"{number_to_check} is not in the range [{start_range},{end_range}]")
