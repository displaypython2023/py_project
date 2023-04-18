import tkinter as tk
import os
from tkinter.filedialog import askopenfile 
import pandas as pd

# added only to define required global variable "txt"
class Txt(object):
    data = None
    def SetValue(self,data): 
        self.data = data
    def GetValue(self): 
        return self.data
txt = Txt()
####

def open():
    file = tk.filedialog.askopenfilename(initialdir= os.getcwd(),
                           title= "Please select a file:") 
    xls = pd.ExcelFile(file)
    df1 = pd.read_excel(xls, 0)
    df2 =xls.parse()
    print(df2)
    if file is not None: 
        txt.SetValue(df2)
    label=tk.Label(win, text=txt.GetValue())
    label.pack()
    
        

def show():
    value  = textField.get()
    name.set(value)
    
win = tk.Tk()
win.title('Text Editor')
win.geometry('500x500')

textField = tk.Entry(win, width=50)
textField.pack(fill=tk.NONE, side=tk.TOP)
#create a label 
name= tk.StringVar(win, value="empty")
label = tk.Label(win, textvariable=name)
label.pack()
# create button to open file
openBtn = tk.Button(win, text='Open', command=open)
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)

# create button to save file
saveBtn = tk.Button(win, text='Show', command=show)
saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)

win.mainloop()