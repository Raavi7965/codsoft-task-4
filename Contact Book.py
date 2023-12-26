import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []

        # Labels
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        # Entry widgets
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("Contact list is empty.")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = []

        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                found_contacts.append(contact)

        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
