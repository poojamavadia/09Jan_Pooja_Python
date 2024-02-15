#Write a Python program to select an item randomly from a list. 
import random

def select_random_item(input_list):
    return random.choice(input_list)

my_list=[1, 2, 3, 4, 5]
random_item=select_random_item(my_list)
print("Randomly selected item:",random_item)
