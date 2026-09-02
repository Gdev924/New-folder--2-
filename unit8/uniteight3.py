import string 
alpha=string.ascii_lowercase
beta=string.ascii_uppercase
mes=input("Please enter a message : \n")
key=int(input("Please enter a shift number\n"))
encrypted_word=""
for letter in mes:
    if letter in alpha:
        original_position=alpha.index(letter)
        new_position=(original_position-key)% 26
        encrypted_word +=alpha[new_position]
    elif letter in beta:
        original_position=beta.index(letter)
        new_position=(original_position+key)% 26
        encrypted_word+=beta[new_position]
    else:
        encrypted_word+=letter
print(f"here is the encrypted word :\n{encrypted_word}")