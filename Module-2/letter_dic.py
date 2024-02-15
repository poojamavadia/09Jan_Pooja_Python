#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
def all_combinations(dictionary):
    combinations=[]
    for value1 in dictionary['1']:
        for value2 in dictionary['2']:
            combinations.append(value1+value2)
    return combinations


data={'1':['a','b'],'2':['c','d']}
result=all_combinations(data)
print("All combinations of letters:")
for combination in result:
    print(combination)
