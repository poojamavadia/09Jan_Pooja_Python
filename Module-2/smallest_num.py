#Write a Python program to find the second smallest number in a list. 
def second_smallest_number(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[1]


numbers_list=[5,2,8,1,9,3]
second_smallest=second_smallest_number(numbers_list)
print("Second smallest number:",second_smallest)
