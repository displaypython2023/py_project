import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("240x240")
root.title('puissance 3')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

for i in range(0,4):
    for j in range(0,4):
        box_pos = ttk.Label(root, text="X")
        box_pos.grid(column=i, row=j, sticky=tk.W, padx=5, pady=5)
root.mainloop()