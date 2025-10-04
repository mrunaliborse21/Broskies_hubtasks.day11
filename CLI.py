import json
import os

class ContactBook:
    def _init_(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def search_contact(self):
        query = input("Enter name or phone number to search: ")
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts found.")

    def delete_contact(self):
        query = input("Enter name or phone number to delete: ")
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts available.")

def main():
    filename = 'contacts.json'
    contact_book = ContactBook(filename)

    while True:
        print("\nContact Book CLI App")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.search_contact()
        elif choice == '3':
            contact_book.delete_contact()
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()
