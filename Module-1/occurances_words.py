#write a python program to count occuranes of each word in a given sentenes.
sentence=input("Enter sentences...")

words=sentence.split()
count={}

for word in words:
    if word not in count:
        count[word]=1
    else:
        count[word]+=1

print("Word Occurances:")
for word,count in count.items():
    print(f"{word}:{count}")
    