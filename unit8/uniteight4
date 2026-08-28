import string

def encrypt(message, shift): 
    alphabet = string.ascii_lowercase
    
    encrypted_message = "" 
    
    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + shift) % 26
            encrypted_letter = alphabet[new_position]
             
            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()
                
            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
            
    print(f"the encrypted message is :\n{encrypted_message}") 

encrypt(message=(input("please enter the message :\n")),shift=int(input("please enter the key:\n")))