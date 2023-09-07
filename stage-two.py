import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

#creates window
window = tk.Tk()
window.geometry('750x400')
window.title('Music Identification')

#creates tab interface
tabs = ttk.Notebook(window)
tabs.pack(fill=BOTH, expand=True)

#create a tab for each screen
login = ttk.Frame(tabs)
signup = ttk.Frame(tabs)

#add screen tabs to tab interface
tabs.add(login, text='Login')
tabs.add(signup, text='Sign up')

window.mainloop()