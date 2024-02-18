import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = {}
        self.create_widgets()
    
    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.save_button = tk.Button(self.root, text="Save Contact", command=self.save_contact)
        self.save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.grid(row=3, column=0, padx=10, pady=10)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        self.contacts_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contacts_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        self.view_all_button = tk.Button(self.root, text="View All Contacts", command=self.view_all_contacts)
        self.view_all_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact saved successfully")
        else:
            messagebox.showerror("Error", "Name and phone number are required")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
    
    def search_contact(self):
        name = self.search_entry.get()
        if name in self.contacts:
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {self.contacts[name]}")
        else:
            messagebox.showerror("Error", "Contact not found")
        self.search_entry.delete(0, tk.END)
    
    def update_contact(self):
        name = self.search_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            if phone:
                self.contacts[name] = phone
                messagebox.showinfo("Success", "Contact updated successfully")
            else:
                messagebox.showerror("Error", "Phone number is required")
        else:
            messagebox.showerror("Error", "Contact not found")
        self.search_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
    
    def delete_contact(self):
        name = self.search_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "Contact not found")
        self.search_entry.delete(0, tk.END)
    
    def view_all_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
