contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for c in contacts:
                print(c["name"], "-", c["phone"])

    elif choice == "3":
        search = input("Enter name or phone to search: ")
        found = False
        for c in contacts:
            if c["name"] == search or c["phone"] == search:
                print(c)
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ")
        for c in contacts:
            if c["name"] == name:
                c["phone"] = input("New Phone: ")
                c["email"] = input("New Email: ")
                c["address"] = input("New Address: ")
                print("Contact updated!")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ")
        for c in contacts:
            if c["name"] == name:
                contacts.remove(c)
                print("Contact deleted!")
                break
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book")
        break

    else:
        print("Invalid choice")