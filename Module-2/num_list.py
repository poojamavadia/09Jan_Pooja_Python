#Write a Python function to get the largest number, smallest num and sum of all from a list.
def my_function(numbers):
    if not numbers:
        return None,None,0
    
    max_num=max(numbers)
    min_num=min(numbers)
    total_sum = sum(numbers)
    
    return max_num, min_num,total_sum

numbers_list=[5,3,9,1,7]
largest,smallest,total=my_function(numbers_list)
print("Largest number:",largest)
print("Smallest number:",smallest)
print("Sum of all numbers:",total)
