from tkinter import *
from tkinter import ttk
class runner:
    name = "init"
    root = None
    frm = None
    label = None
    def __init__(self,text,root,frm):
        self.name =text
        self.root =root
        self.frm =frm
    def dont_do_this(self):
        ttk.Button(self.frm, text=self.name, command=self.root.destroy).grid(column=1, row=0)
       

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="don't click please!").grid(column=0, row=0)
run_me = runner("how dare you to click",root,frm)
ttk.Button(frm, text="don't do it !!!!!!", command=run_me.dont_do_this).grid(column=1, row=0)
root.mainloop()