the_items_names=[]
the_prices=[]
print("welcom to ishop calculator\n")
a=int(input("please enter how many items are in your basket today"))
print("let's count them..\n")
for b in range(1,a+1):
    c=input(f" tell me the name of item number {b}")
    the_items_names.append(c)
    d=float(input(f"how much does {c} cost ?"))
    the_prices.append(d)
e=input("do you like to see your entire basket items ? (yes/no)").lower()
if e=="yes":
    print(f"{the_items_names}")
elif e=="no":
    print("why tf did i wrote this whole goddamn code so ?")
f=input("do you like to see how much does it cost in total ? (yes/no)").lower()
if f=="yes":
    print(f" it costs {sum(the_prices)}")