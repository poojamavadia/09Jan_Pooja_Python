#Write a Python program to combine values in python list of dictionaries. 
def combine_values(list_of_dicts):
    combined_values={}
    for d in list_of_dicts:
        item=d['item']
        amount=d['amount']
        combined_values[item]=combined_values.get(item, 0)+amount
    return combined_values

sample_data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
result=combine_values(sample_data)
print("Combined values in the list of dictionaries:")
print(result)
