#contact list:
contactList = []

#get user input
def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contact = name, number
    #print(contact)
    contactList.append(contact)
    

def show_contact(contactList):
    print(contactList)

def delete_contact(contactList):
    choice = input("Enter the name of contact you would like to delete.")
    #selected
    for contact in contactList:
        if choice == contact.name:
            contactList.remove(contact)
    print(f"You removed ${contact} from list.")
 