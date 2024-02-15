#Write a Python program to combine two dictionary adding values for common keys. 
def combine_dicts(d1, d2):
    combined={}
    for key in d1.keys()|d2.keys():
        combined[key] = d1.get(key,0)+d2.get(key, 0)
    return combined


d1={'a':100,'b': 200,'c':300}
d2={'a':300,'b': 200,'d':400}

combined_dict = combine_dicts(d1, d2)
print("Combined dictionary with values for common keys added:", combined_dict)
