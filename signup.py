import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

import csv

def signup_frame(parent, window, start_frame, main_frame, screen_height, screen_width):
  signup = Frame(parent)
  style = Style(theme='superhero')

  #labels
  signup_lheader = ttk.Label(signup, text='SIGN UP', font=('Leelawadee', 20))
  signup_lusername = ttk.Label(signup, text='Username', font=('Leelawadee', 11))
  signup_lpassword = ttk.Label(signup, text='Password', font=('Leelawadee', 11))
  signup_error = ttk.Label(signup, text='', font=('Leelawadee', 9), style='danger.TLabel')

  #entries
  signup_eusername = ttk.Entry(signup, textvariable=StringVar, font=('Leelawadee', 11), width=29, justify=CENTER, style='primary.TEntry')
  signup_epassword = ttk.Entry(signup, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry', show='*')


  def sign_up():
    dict = {'USERNAME': signup_eusername.get(), 'PASSWORD': signup_epassword.get()}

    with open('login.csv', 'a') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=['USERNAME', 'PASSWORD'])
      writer.writerow(dict)
      csvfile.close()

    main_frame.pack(fill=BOTH, expand=True)
    x = (screen_width/2) - (750/2)
    y = (screen_height/2) - (400/2)
    window.geometry('%dx%d+%d+%d' % (750, 400, x, y))
    start_frame.pack_forget()
    signup_error.config(text='')

  def check_user():
    special_characters = "!@#$%^&*()-+?_=,<>/\"\'"
    if signup_eusername.get() != '':
      if not any(char in special_characters for char in signup_eusername.get()):
        with open('login.csv', 'r') as csvfile:
          reader = csv.DictReader(csvfile)
          exists = False
          for row in reader:
            if signup_eusername.get() == row['USERNAME']:
              exists = True
              break
            else:
              exists = False
            
          if exists:
            signup_error.config(text='User already exists.\nTry logging in.')
          else:
            if signup_epassword.get() == '':
              signup_error.config(text='Please enter a password.')
              signup_epassword.focus()
            else:
              if not any(char in special_characters for char in signup_epassword.get()):
                sign_up() 
              else:
                signup_error.config(text='Your password may only contain alphanumeric characters')
      else:
        signup_error.config(text='Your username may only contain alphanumeric characters')
    else:
      signup_error.config(text='Please enter a username')

  signup_button = ttk.Button(signup, text='Create account', style='primary.Outline.TButton', command=check_user, cursor='hand2')

  #checkbox
  signup_checked = tk.IntVar()

  def signup_showpassword():
    if signup_checked.get():
      signup_epassword.config(show='')
    else:
      signup_epassword.config(show='*')

  signup_checkbox = ttk.Checkbutton(signup, command=signup_showpassword, variable=signup_checked, onvalue=1, offvalue=0, cursor='hand2', style='primary.Squaretoggle.Toolbutton')

  #add elements to signup
  signup_lheader.place(relx=0.5,y=35,anchor=CENTER)
  signup_lusername.place(x=30,y=68)
  signup_eusername.place(relx=0.5,y=106,anchor=CENTER)
  signup_lpassword.place(x=30,y=138)
  signup_epassword.place(relx=0.45,y=176, anchor=CENTER)
  signup_button.place(relx=0.5,y=230,anchor=CENTER)
  signup_checkbox.place(relx=0.875,y=176,anchor=CENTER)
  signup_error.place(relx=0.5,y=270,anchor=CENTER)

  return signup