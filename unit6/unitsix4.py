a=input("enter the 1st and the last name of ur friends separated by comma ").split(",")
print("\n".join(a))
c=len(a)
for b in range(c) :
    d= a[b].split(" ")
    print(f"{d[0][0].capitalize()};{d[1][0].capitalize()}")