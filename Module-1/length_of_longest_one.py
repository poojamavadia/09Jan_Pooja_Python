#write a python function that takes a list of words and returns the length of longest one.
def f(word):
    
    if not word:
        return 0  
    max_length = len(word[0])
    
    for word in word[1:]:
        current_length=len(word)
        if current_length>max_length:
            max_length=current_length
    
    return max_length

word=input("Enter a list of words separated by spaces: ").split()
result= f(word)
print("Length of the longest word:",result)
