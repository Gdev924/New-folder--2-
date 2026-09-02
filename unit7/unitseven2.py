import random
words=["office","panda","cabin","ginger"]
random_word=random.choice(words)
guess=input("pls guess a letter\n").lower()
for x in random_word:
    if guess == random_word[x]:
        print("right")
    else:
        print("wrong")