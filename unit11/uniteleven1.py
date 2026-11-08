contacts = {} 
print("Contact Management:\n") 
while True: 
    print("""
    1-add a contact 
    2-edit a contact 
    3-view contact 
    4-exit""")     
    a = input("Please choose a number between 1-4 :\n") 
    if a == "1": 
        contact_id = input("Please input the ID of the new contact..\n") 
        contact_name = input("Please input the name of the new contact..\n") 
        contact_phone = input("Please input the phone number of the new contact..\n") 
        contacts[contact_id] = {"name": contact_name, "phone": contact_phone} 
        print("success...") 
    elif a == "2": 
        while True: 
            id_to_edit = input("please enter the id to edit \n") 
            if id_to_edit.isdigit(): 
                if id_to_edit in contacts: 
                    new_name = input("please enter the new name\n") 
                    new_phone = input("please enter the new phone\n") 
                    contacts[id_to_edit]["name"] = new_name 
                    contacts[id_to_edit]["phone"] = new_phone 
                    
                    print("success...") 
                    break
                else: 
                    print("sorry , there is no id like that !") 
                    break 
            else: 
                print("enter digits only...") 
    elif a == "3": 
        print(contacts) 
        
    elif a == "4": 
        print("Exiting the program...") 
        break 
        
    else: 
        print("Invalid input...")