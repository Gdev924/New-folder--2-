import string
a=input("\n please enter a sentence \n")
new_sen=""
for b in a :
    if b not in string.punctuation:
     new_sen += b 
print("your sentence without punctuation is "+ new_sen )