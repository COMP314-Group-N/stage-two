import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import csv

#creates window
window = tk.Tk()
style = ttk.Style()
window.title('Music Identification')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
 
x = (screen_width/2) - (300/2)
y = (screen_height/2) - (300/2)
 
window.geometry('%dx%d+%d+%d' % (300, 300, x, y))

#creates frames for each screen
start = Frame(window)
main = Frame(window)

start.pack(fill=BOTH, expand=True)

#creates tab interface
tabs = ttk.Notebook(start)
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
login_error = Label(login, text='', font=('Ubuntu', 9), bg='#DDE6ED', fg='red')

#entries
login_eusername = ttk.Entry(login, textvariable=StringVar, font=('Ubuntu', 11), width=29, justify=CENTER)
login_epassword = ttk.Entry(login, textvariable=StringVar, font=('Ubuntu', 11), width=29, justify=CENTER, show='*')

#button
def check_login():
  with open('login.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    exists = False
    for row in reader:
      if login_eusername.get() == row['USERNAME']:
        if login_epassword.get() == row['PASSWORD']:
          main.pack(fill=BOTH, expand=True)

          x = (screen_width/2) - (500/2)
          y = (screen_height/2) - (300/2)
 
          window.geometry('%dx%d+%d+%d' % (500, 300, x, y))

          start.pack_forget()
          login_error.config(text='')
        else:
          login_error.config(text='Incorrect password.')

        exists = True
        break

    if exists == False:
      login_error.config(text = 'Login details not found.\nRe-enter details or try signing up.')

login_button = ttk.Button(login, text='Log in', style='login_button.TButton', command=check_login, cursor='hand2')

style.configure('login_button.TButton', font=('Ubuntu', 11), justify=CENTER)

#add elements to login
login_lheader.place(relx=0.5,y=45,anchor=CENTER)
login_lusername.place(x=30,y=70)
login_eusername.place(relx=0.5,y=108,anchor=CENTER)
login_lpassword.place(x=30,y=130)
login_epassword.place(relx=0.5,y=168,anchor=CENTER)
login_button.place(relx=0.5,y=215,anchor=CENTER)
login_error.place(relx=0.5,y=250,anchor=CENTER)

window.mainloop()