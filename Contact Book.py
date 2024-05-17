class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone_number}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("Search results:")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone_number = input("Enter new phone number: ")
                contact.phone_number = new_phone_number
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            address_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == '2':
            address_book.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            address_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            address_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            address_book.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
