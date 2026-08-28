import string

def decrypt(message, shift): # Change function name to decrypt
    alphabet = string.ascii_lowercase
    
    decrypted_message = "" 
    
    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            # Change to subtraction
            new_position = (original_position - shift) % 26
            decrypted_letter = alphabet[new_position]
             
            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()
                
            decrypted_message += decrypted_letter
        else:
            decrypted_message += letter
            
    print(f"the message is :\n{decrypted_message}") 

decrypt(message=input("please enter the encrypted message:\n"),shift=int(input("please enter the key:\n")))