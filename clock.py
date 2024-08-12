# CREATE A DIGITAL CLOCK BY USING PYTHON


import tkinter as tk
from time import strftime

root = tk.Tk()

# To show a tittle 
root.title("DIGITAL CLOCK")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    lable.config(text=string)

    # Update time every second
    lable.after(1000,time)
    
lable = tk.Label(root, font=('calibri', 50, 'bold'), background='purple', foreground='black')
lable.pack(anchor='center')

time()

root.mainloop()