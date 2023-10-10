import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

from tinydb import TinyDB, Query

db = TinyDB('login.json')
query = Query()

class SignUp(tk.Frame):
  def __init__(self, master):
    master.title('Sign up')

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
    lheader = ttk.Label(self, text='SIGN UP', font=('Leelawadee', 20))
    lusername = ttk.Label(self, text='Username', font=('Leelawadee', 11))
    lpassword = ttk.Label(self, text='Password', font=('Leelawadee', 11))
    error = ttk.Label(self, text='', font=('Leelawadee', 9), style='danger.TLabel', justify=CENTER)
    #====================

    #entries=============
    eusername = ttk.Entry(self, textvariable=StringVar, font=('Leelawadee', 11), width=29, justify=CENTER, style='primary.TEntry')
    epassword = ttk.Entry(self, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry', show='*')
    #====================

    #adds new user details to login.json
    def sign_up():
      db.insert({'username': eusername.get(), 'password': epassword.get()})
      error.config(text='')

      master.switch_frame("AudioGen")
    #====================

    #checks if user exists in login.json
    def check_user():
      special_characters = "!@#$%^&*()-+?_=,<>/\"\'"
      if eusername.get() != '':
        if not any(char in special_characters for char in eusername.get()):
          if not db.search(query.username == eusername.get()):
            if epassword.get() == '':
              error.config(text='Please enter a password.')
              epassword.focus()
            else:
              if not any(char in special_characters for char in epassword.get()):
                sign_up() 
              else:
                error.config(text='Your password may only contain alphanumeric characters')
          else:
            error.config(text='User already exists')
        else:
          error.config(text='Only alphanumeric characters allowed')
      else:
        error.config(text='Please enter a username')
    #====================

    #buttons=============
    bsignup = ttk.Button(self, text='Create account', style='primary.Outline.TButton', command=check_user, cursor='hand2')

    blogin = ttk.Button(self, text='<- Login', style='primary.Outline.TButton', cursor='hand2', command=lambda: master.switch_frame("Login"))
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

    #add elements to signup
    lheader.place(relx=0.5,y=40,anchor=CENTER)
    lusername.place(x=30,y=73)
    eusername.place(relx=0.5,y=111,anchor=CENTER)
    lpassword.place(x=30,y=143)
    epassword.place(relx=0.45,y=181, anchor=CENTER)
    bsignup.place(relx=0.35,y=235,anchor=CENTER)
    checkbox.place(relx=0.875,y=181,anchor=CENTER)
    error.place(relx=0.5,y=275,anchor=CENTER)
    blogin.place(relx=0.71, y=235, anchor=CENTER)
    #====================

if __name__ == "__main__":
    app = SignUp()
    app.mainloop()