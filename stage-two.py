import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import pandas as pd

#creates window
window = tk.Tk()
style = ttk.Style()
window.title('Music Identification')
window.geometry('300x300+800+350')
window.configure(bg='#DDE6ED')
window.resizable(width=False,height=False)

#creates tab interface
tabs = ttk.Notebook(window)
tabs.pack(fill=BOTH, expand=True)

#create a tab for each screen
login = Frame(tabs, bg='#DDE6ED')
signup = Frame(tabs, bg='#DDE6ED')

#add screen tabs to tab interface
tabs.add(login, text='Login')
tabs.add(signup, text='Sign up')

#LOGIN
#labels
login_lheader = Label(login, text='LOGIN', font=('Ubuntu', 20), bg='#DDE6ED')
login_lusername = Label(login, text='Username', font=('Ubuntu', 11), bg='#DDE6ED')
login_lpassword = Label(login, text='Password', font=('Ubuntu', 11), bg='#DDE6ED')

#entries
login_eusername = ttk.Entry(login, textvariable=StringVar, font=('Ubuntu', 11), width=29, justify=CENTER)
login_epassword = ttk.Entry(login, textvariable=StringVar, font=('Ubuntu', 11), width=29, justify=CENTER, show='*')

#button
def check_login():
  file = pd.read_csv('login.csv', usercols=['Username','Password'])
  login_eusername.insert(0, file)

login_button = ttk.Button(login, text='Log in', style='login_button.TButton', command=check_login, cursor='hand2')

style.configure('login_button.TButton', font=('Ubuntu', 11), justify=CENTER)

#add elements to login
login_lheader.place(x=110,y=25)
login_lusername.place(x=30,y=70)
login_eusername.place(x=30,y=95)
login_lpassword.place(x=30,y=130)
login_epassword.place(x=30,y=155)
login_button.place(x=100, y=200)

window.mainloop()