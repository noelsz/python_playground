import os


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


    def __str__(self):
        return f"Name: {self.name}\nE-mail: {self.email}\nPhone: {self.phone}\n"


class ContactList:
    def __init__(self):
        self.contacts = []


    def add_contact(self, contact):
        self.contacts.append(contact)


    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contacts(self, info):
        result = None
        for contact in self.contacts:
            if info in contact.name or info in contact.email or info in contact.phone:
                result = contact
        return result

    def view_contacts(self):
        for contact in self.contacts:
            print(str(contact) + "\n")


def contact_list(contacts):
    print("--- Contact List ---")
    print("1. View your contacts \n2. Add a contact \n3. Remove a contact \n4. Search for a contact\n")
    choice = int(input("Press the number of your choice: "))
    if choice:
        match choice:
            case 1:
                return view_contacts(contacts)
            case 2:
                return add_to_list(contacts)
            case 3:
                return remove_from_list(contacts)
            case 4:
                return search_in_list(contacts)
    else:
        print("No choice, exiting program...")
        return


def view_contacts(contacts):
    print("--- Contact List ---")
    contacts.view_contacts()
    input("Press any key to continue...")

    os.system('cls')
    contact_list(contacts)


def add_to_list(contacts):
    name = input("Name of the contact: ")
    email = input("E-mail address of the contact: ")
    phone = input("Phone number of the contact: ")
    contact = Contact(name, email, phone)
    contacts.add_contact(contact)

    os.system('cls')
    contact_list(contacts)


def remove_from_list(contacts):
    info = input("Name / E-mail / Phone number of the contact you want to remove: ")
    result_contact = contacts.search_contacts(info)
    contacts.remove_contact(result_contact)

    os.system('cls')
    contact_list(contacts)


def search_in_list(contacts):
    info = input("Name / E-mail / Phone number of the contact you want to find: ")
    result_contact = contacts.search_contacts(info)
    print(result_contact)
    input("Press any key to continue...")

    os.system('cls')
    contact_list(contacts)

my_contact_list = ContactList()
contact_list(my_contact_list)