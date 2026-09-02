finnished=[]
unfinnished=[]
tasks=input("enter your tasks for today separated by comma").split(", ")
for task in tasks :
    print(f"\n{task}..\n")
    a=input("did you finish that task already ? (yes/no) \n").lower()
    if a=="yes":
        print("Good job..\n")
        finnished.append(task)
    elif a=="no":
        print("try not to put it off..\n")
        unfinnished.append(task)

b=input("Do you want to see today's progress ? (yes/no) \n").lower()
if b=="yes":
    print(f"done tasks are : {finnished}\nongoing tasks are {unfinnished}.\n")

input("press enter to exit..")