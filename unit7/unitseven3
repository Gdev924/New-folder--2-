import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ["shadow", "galaxy", "matrix", "wizard", "python", "coffee", "guitar", "castle", "pirate", "jungle","astronaut", "dinosaur", "adventure", "spaceship", "chocolate", "nightmare", "butterfly", "pineapple","pizza", "lucky", "funny", "puppy", "toxic", "cyber", "quiz"]
random_word = random.choice(words)
display=["_"for y in random_word]
tries=6
allthelets=[]
while "_" in display and tries>0:
    guess = input("pls guess a letter\n").lower()    
    if guess in allthelets:
        print("you already guessed this ,try again..")
        continue
    allthelets.append(guess)
    for x in range(len(random_word)):
        if guess == random_word[x]:
            display[x] = guess           
    if guess not in random_word:
        tries-=1
    print(" ".join(display))
    print(f"you have {tries} tries left ")
    if tries<6 :
       print(HANGMANPICS[5-tries])

if tries == 0:
    print(f"""you lose !, the word was *{random_word}*
""")
else :
    print(f"                     YOU WON ! the word was *{random_word}*")