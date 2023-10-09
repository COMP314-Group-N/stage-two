import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

from tinydb import TinyDB, Query

db = TinyDB('./login.json')
query = Query()

class Login(tk.Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    style = Style(theme='superhero')

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = (screen_width/2) - (310/2)
    y = (screen_height/2) - (340/2)
    master.geometry('%dx%d+%d+%d' % (310, 340, x, y))
    self.pack(fill=BOTH, expand=True)

    #labels==============
    lheader = ttk.Label(self, text='LOGIN', font=('Leelawadee', 20))
    lusername = ttk.Label(self, text='Username', font=('Leelawadee', 11))
    lpassword = ttk.Label(self, text='Password', font=('Leelawadee', 11))
    error = ttk.Label(self, text='', font=('Leelawadee', 9), style='danger.TLabel', justify=CENTER)
    #====================

    #entries=============
    eusername = ttk.Entry(self, textvariable=StringVar, font=('Leelawadee', 11), width=29, justify=CENTER, style='primary.TEntry')
    epassword = ttk.Entry(self, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry', show='*')
    #====================

    #button==============
    def check_login():
      if (db.search(query.username == eusername.get())):
        if (db.search((query.username == eusername.get()) & 
                      (query.password == epassword.get()))):
          error.config(text='')

          master.switch_frame("AudioGen")
        else: 
          error.config(text='Incorrect password')
      else:
        error.config(text='User does not exist')      

    button = ttk.Button(self, text='Log in', style='primary.Outline.TButton', cursor='hand2', command=check_login)

    style.configure('primary.Outline.TButton', font=('Leelawadee', 11), justify=CENTER)
    #====================

    #checkbox============
    checked = tk.IntVar()

    def show_password():
      if checked.get():
        epassword.config(show='')
      else:
        epassword.config(show='*')

    checkbox = ttk.Checkbutton(self, command=show_password, variable=checked, onvalue=1, offvalue=0, cursor='hand2', style='primary.Squaretoggle.Toolbutton')
    #====================

    #add elements to login
    lheader.place(relx=0.5,y=35,anchor=CENTER)
    lusername.place(x=30,y=68)
    eusername.place(relx=0.5,y=106,anchor=CENTER)
    lpassword.place(x=30,y=138)
    epassword.place(relx=0.45,y=176, anchor=CENTER)
    button.place(relx=0.5,y=230,anchor=CENTER)
    checkbox.place(relx=0.875,y=176,anchor=CENTER)
    error.place(relx=0.5,y=270,anchor=CENTER)
    #====================

if __name__ == "__main__":
  app = Login()
  app.mainloop()