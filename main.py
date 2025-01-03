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
 
def main():
    answer = input("Welcome to your personal contact book. To add contact, press 1 . To delete contact, press 2 . To preview available contacts, press 3 .")
    if answer == "1":
        add_contact()
        main()
    if answer == "2":
        delete_contact(contactList)
        main()
    if answer == "3":
        show_contact(contactList)
        main()
    else:
        print("Please enter valid selection")
        main()

main()