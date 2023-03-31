import tkinter as tk

root = tk.Tk()


label = tk.Label(root, text="Hello World")

label.grid(row=2, column=5)

for row in range(4):
    root.grid_rowconfigure(row, minsize=8)
    for col in range(4):
        root.grid_columnconfigure(col, minsize=8)


root.mainloop()