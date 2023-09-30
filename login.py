import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

import csv

def login_frame(parent, window, start_frame, main_frame, screen_height, screen_width):
  login = Frame(parent)
  style = Style(theme='superhero')

  #labels==============
  login_lheader = ttk.Label(login, text='LOGIN', font=('Leelawadee', 20))
  login_lusername = ttk.Label(login, text='Username', font=('Leelawadee', 11))
  login_lpassword = ttk.Label(login, text='Password', font=('Leelawadee', 11))
  login_error = ttk.Label(login, text='', font=('Leelawadee', 9), style='danger.TLabel', justify=CENTER)
  #====================

  #entries=============
  login_eusername = ttk.Entry(login, textvariable=StringVar, font=('Leelawadee', 11), width=29, justify=CENTER, style='primary.TEntry')
  login_epassword = ttk.Entry(login, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry', show='*')
  #====================

  #button==============
  def check_login():
    with open('login.csv', 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      exists = False
      for row in reader:
        if login_eusername.get() == row['USERNAME']:
          if login_epassword.get() == row['PASSWORD']:
            main_frame.pack(fill=BOTH, expand=True)
            x = (screen_width/2) - (525/2)
            y = (screen_height/2) - (400/2)
            window.geometry('%dx%d+%d+%d' % (525, 400, x, y))

            start_frame.pack_forget()
            login_error.config(text='')

            login_eusername.delete(0, END)
            login_epassword.delete(0, END)
            signup_eusername.delete(0, END)
            signup_epassword.delete(0, END)
          else:
            login_error.config(text='Incorrect password.')

          exists = True
          break

      if exists == False:
        login_error.config(text = 'User does not exist.\nRe-enter details or try signing up.')

  login_button = ttk.Button(login, text='Log in', style='primary.Outline.TButton', command=check_login, cursor='hand2')

  style.configure('primary.Outline.TButton', font=('Leelawadee', 11), justify=CENTER)
  #====================

  #checkbox============
  login_checked = tk.IntVar()

  def login_showpassword():
    if login_checked.get():
      login_epassword.config(show='')
    else:
      login_epassword.config(show='*')

  login_checkbox = ttk.Checkbutton(login, command=login_showpassword, variable=login_checked, onvalue=1, offvalue=0, cursor='hand2', style='primary.Squaretoggle.Toolbutton')
  #====================

  #add elements to login
  login_lheader.place(relx=0.5,y=35,anchor=CENTER)
  login_lusername.place(x=30,y=68)
  login_eusername.place(relx=0.5,y=106,anchor=CENTER)
  login_lpassword.place(x=30,y=138)
  login_epassword.place(relx=0.45,y=176, anchor=CENTER)
  login_button.place(relx=0.5,y=230,anchor=CENTER)
  login_checkbox.place(relx=0.875,y=176,anchor=CENTER)
  login_error.place(relx=0.5,y=270,anchor=CENTER)
  #====================

  return login