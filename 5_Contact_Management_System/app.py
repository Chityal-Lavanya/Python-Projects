import json


FILE_NAME = "5_Contact_Management_System/contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)

    print("Contact added successfully!")


# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        contact = contacts[name]

        print("\n===== CONTACT DETAILS =====")
        print("Name :", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    else:
        print("Contact not found!")


# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== ALL CONTACTS =====")

    for name, contact in contacts.items():
        print(f"\nName : {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


# Update contact
def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    print("\n1. Update Phone")
    print("2. Update Email")
    print("3. Update Both")

    choice = input("Enter your choice: ")

    if choice == "1":
        contacts[name]["phone"] = input("Enter new phone number: ").strip()

    elif choice == "2":
        contacts[name]["email"] = input("Enter new email: ").strip()

    elif choice == "3":
        contacts[name]["phone"] = input("Enter new phone number: ").strip()
        contacts[name]["email"] = input("Enter new email: ").strip()

    else:
        print("Invalid choice!")
        return

    save_contacts(contacts)

    print("Contact updated successfully!")


# Delete contact
def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]

        save_contacts(contacts)

        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# Main program
contacts = load_contacts()

while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        search_contact(contacts)

    elif choice == "3":
        view_contacts(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("Contacts saved. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")