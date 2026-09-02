import random
names_string=input("enter ur friends names separated by coma .., good friend(:")
names=names_string.split(", ")
length = len(names)-1
random_number= random.randint(0,length)
the_unlucky_guy=names[random_number]
print(f"tell our poor dude {the_unlucky_guy} to take his wallet out , the dinner id on him tonight!")