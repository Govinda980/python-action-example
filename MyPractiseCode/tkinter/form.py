import tkinter as tk
from tkinter import messagebox


def show_full_name():
    name = name_Entry.get()
    age = age_Entry.get()
    if name and age:
        messagebox.showinfo("Form submitted", f"my name is {name} and age is {age}")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")


root = tk.Tk()
root.geometry('400x500')
root.title("My first application")
tk.Label(root, text='Name').grid(row=0)
name_Entry = tk.Entry(root)
name_Entry.grid(row=0, column=1)

tk.Label(root, text='Age').grid(row=1)
age_Entry = tk.Entry(root)
age_Entry.grid(row=1, column=1)

tk.Button(root, text="show full name", command=show_full_name).grid(row=7, column=1)

root.mainloop()
