class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Store Name: {self.store_name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone_number, email, address):
        new_contact = Contact(store_name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{store_name}' added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)


def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(store_name, phone_number, email, address)
        elif choice == '2':
            manager.display_contacts()
        elif choice == '3':
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
