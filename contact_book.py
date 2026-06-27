import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

contacts = []

if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        contacts = []

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def refresh_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(
            tk.END,
            f"{contact['name']} | {contact['phone']}"
        )



def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Name and Phone are required."
        )
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts()
    refresh_list()
    clear_fields()

    messagebox.showinfo("Success", "Contact Added Successfully.")



def delete_contact():
    try:
        index = contact_list.curselection()[0]
        contacts.pop(index)

        save_contacts()
        refresh_list()
        clear_fields()

        messagebox.showinfo("Deleted", "Contact Deleted.")

    except:
        messagebox.showwarning("Warning", "Select a contact.")


def search_contact():
    keyword = name_entry.get().lower()

    contact_list.delete(0, tk.END)

    for contact in contacts:
        if keyword in contact["name"].lower():
            contact_list.insert(
                tk.END,
                f"{contact['name']} | {contact['phone']}"
            )



def show_contact(event):
    try:
        index = contact_list.curselection()[0]

        contact = contacts[index]

        clear_fields()

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])

    except:
        pass



def update_contact():
    try:
        index = contact_list.curselection()[0]

        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }

        save_contacts()
        refresh_list()

        messagebox.showinfo("Success", "Contact Updated.")

    except:
        messagebox.showwarning("Warning", "Select a contact.")



root = tk.Tk()

root.title("Contact Book - CodSoft Internship")
root.geometry("700x600")
root.configure(bg="#EAF4FC")

title = tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 20, "bold"),
    bg="#EAF4FC",
    fg="navy"
)
title.pack(pady=10)



tk.Label(root, text="Name", bg="#EAF4FC").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone", bg="#EAF4FC").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email", bg="#EAF4FC").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address", bg="#EAF4FC").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()



button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add",
    bg="green",
    fg="white",
    width=10,
    command=add_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    bg="blue",
    fg="white",
    width=10,
    command=update_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    bg="red",
    fg="white",
    width=10,
    command=delete_contact
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Search",
    bg="orange",
    fg="white",
    width=10,
    command=search_contact
).grid(row=0, column=3, padx=5)

tk.Button(
    button_frame,
    text="Show All",
    bg="purple",
    fg="white",
    width=10,
    command=refresh_list
).grid(row=0, column=4, padx=5)



contact_list = tk.Listbox(root, width=70, height=15)
contact_list.pack(pady=10)

contact_list.bind("<<ListboxSelect>>", show_contact)

refresh_list()

root.mainloop()