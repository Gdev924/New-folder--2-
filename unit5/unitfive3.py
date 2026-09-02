list=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
print(f"welcom in place the rabbit.\n where should the rabbit go ? 🐇 \n\n{list[0]}\n{list[1]}\n{list[2]}\n")
a=input ("please enter the number of a row and a column")
row=int(a[0])
column=int(a[1])
if len(a)!=2 or row==0 or column==0:
    print("sorry , this option is not valide!")
else :
    print("success..\n")
    list[row-1][column-1]="🐇"
    print(f"{list[0]}\n{list[1]}\n{list[2]}\n")