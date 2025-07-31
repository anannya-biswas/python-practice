import json

contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    save_contacts()
    print("Contact saved.")

def search_contact():
    name = input("Enter name to search: ")
    phone = contacts.get(name)
    if phone:
        print(f"{name}: {phone}")
    else:
        print("Contact not found.")

load_contacts()
while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        break
