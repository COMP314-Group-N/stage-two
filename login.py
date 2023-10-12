import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

from tinydb import TinyDB, Query

db = TinyDB('login.json')
query = Query()

class Login(tk.Frame):
  def __init__(self, master):
    master.title('Login')
    master.resizable(False, False)

    Frame.__init__(self, master)
    self.config(highlightthickness=1, highlightbackground='#7F8B96')
    style = Style(theme='superhero')

    w = master.winfo_screenwidth()
    h = master.winfo_screenheight()
    x = (w/2) - (310/2)
    y = (h/2) - (320/2)
    master.geometry('%dx%d+%d+%d' % (310, 320, x, y))
    self.pack(fill=BOTH, expand=True, padx=5, pady=5)

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

    #check login details by querying login.json
    def check_login():
      if (db.search(query.username == eusername.get())):
        if (db.search((query.username == eusername.get()) & 
                      (query.password == epassword.get()))):
          error.config(text='')

          master.switch_frame("Genre")
        else: 
          error.config(text='Incorrect password')
      else:
        error.config(text='User does not exist')      
    #====================

    #buttons=============
    blogin = ttk.Button(self, text='Log in', style='primary.Outline.TButton', cursor='hand2', command=check_login)

    bsignup = ttk.Button(self, text='Sign up ->', style='primary.Outline.TButton', cursor='hand2', command=lambda: master.switch_frame("SignUp"))
    #====================

    #checkbox============
    checked = tk.IntVar()

    def show_password(): #toggles password characters (*)
      if checked.get():
        epassword.config(show='')
      else:
        epassword.config(show='*')

    checkbox = ttk.Checkbutton(self, command=show_password, variable=checked, onvalue=1, offvalue=0, cursor='hand2', style='primary.Squaretoggle.Toolbutton')
    #====================

    #add elements to frame
    lheader.place(relx=.5, y=40, anchor=CENTER)
    lusername.place(x=30, y=73)
    eusername.place(relx=.5, y=111, anchor=CENTER)
    lpassword.place(x=30, y=143)
    epassword.place(relx=.45, y=181, anchor=CENTER)
    blogin.place(relx=.325, y=235, anchor=CENTER)
    checkbox.place(relx=.875, y=181, anchor=CENTER)
    error.place(relx=.5, y=275, anchor=CENTER)
    bsignup.place(relx=.625, y=235, anchor=CENTER)
    #====================

if __name__ == "__main__":
  app = Login()
  app.mainloop()