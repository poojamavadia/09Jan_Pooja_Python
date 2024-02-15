#Write a Python program to find the repeated items of a tuple.
def find_repeated_items(input_tuple):
    item_counts = {}
    for item in input_tuple:
        if item in item_counts:
            item_counts[item]+=1
        else:
            item_counts[item] = 1
    repeated_items=[]
    
    for item, count in item_counts.items():
        if count > 1:
            repeated_items.append(item)
    
    return repeated_items


my_tuple=(1, 2, 3, 4, 2, 3, 5, 2)
repeated_items=find_repeated_items(my_tuple)
print("Repeated items in the tuple:",repeated_items)
