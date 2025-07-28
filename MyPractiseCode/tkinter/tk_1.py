import tkinter as tk

root = tk.Tk()
root.geometry('200x300')
root.title('Hello Govinda')

tk.Label(root, text='Name:').grid(row=0)
name = tk.Entry(root)
name.grid(row=0, column=1)
tk.Label(root, text='Age:').grid(row=1)
age = tk.Entry(root)
age.grid(row=1, column=1)

root.mainloop()
