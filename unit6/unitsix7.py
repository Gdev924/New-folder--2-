import random
import string
print("\nwelcom to the password generator, \n")
a=input("please enter how many characters do you want in the password ")
b=int(input("how many letters ?\n"))
c=int(input("how many numbers ?\n"))
d=int(input("how many symbols ?\n"))
if int(b)+int(c)+int(d) != int(a):
    print("invalid input , the sum of the letters , the numbers and the symbols dont match the number of the characters you want \n")

else:
    the_ran_let=random.choices(string.ascii_letters,k=int(b))
    the_ran_dig=random.choices(string.digits, k=int(c))
    the_ran_sym=random.choices(string.punctuation, k=int(d))
    password_list=the_ran_let+the_ran_dig+the_ran_sym
    random.shuffle(password_list)
    the_final_password = "".join(password_list)
    print(f"your password is: {the_final_password}")