#GUI imports
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog as fd

#functional imports
import csv

#WINDOW
##################################################
#creates window
window = tk.Tk()
style = ttk.Style()
window.title('Music Identification')

#center window
#**************************************************
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
 
x = (screen_width/2) - (750/2)
y = (screen_height/2) - (400/2)
 
window.geometry('%dx%d+%d+%d' % (750, 400, x, y))
#**************************************************

#creates frames for each screen
start_frame = Frame(window)
main_frame = Frame(window)

#**************************************************
main_frame.pack(fill=BOTH, expand=True)
#**************************************************

#creates tab interface
tabs = ttk.Notebook(start_frame)
tabs.pack(fill=BOTH, expand=True)

#create a tab for each screen
login = Frame(tabs, bg='#DDE6ED')
signup = Frame(tabs, bg='#DDE6ED')

#add screen tabs to tab interface
tabs.add(login, text='Login')
tabs.add(signup, text='Sign up')
##################################################

#LOGIN
##################################################
#labels
login_lheader = Label(login, text='LOGIN', font=('Ubuntu', 20), bg='#DDE6ED')
login_lusername = Label(login, text='Username', font=('Ubuntu', 11), bg='#DDE6ED')
login_lpassword = Label(login, text='Password', font=('Ubuntu', 11), bg='#DDE6ED')
login_error = Label(login, text='', font=('Ubuntu', 9), bg='#DDE6ED', fg='red')

#entries
login_eusername = ttk.Entry(login, textvariable=StringVar, font=('Ubuntu', 11), width=29, justify=CENTER)
login_epassword = ttk.Entry(login, textvariable=StringVar, font=('Ubuntu', 11), width=25, justify=CENTER, show='*')

#button
def check_login():
  with open('login.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    exists = False
    for row in reader:
      if login_eusername.get() == row['USERNAME']:
        if login_epassword.get() == row['PASSWORD']:
          main_frame.pack(fill=BOTH, expand=True)
          x = (screen_width/2) - (750/2)
          y = (screen_height/2) - (400/2)
          window.geometry('%dx%d+%d+%d' % (750, 400, x, y))

          start_frame.pack_forget()
          login_error.config(text='')
        else:
          login_error.config(text='Incorrect password.')

        exists = True
        break

    if exists == False:
      login_error.config(text = 'User does not exist.\nRe-enter details or try signing up.')

login_button = ttk.Button(login, text='Log in', style='button.TButton', command=check_login, cursor='hand2')

style.configure('button.TButton', font=('Ubuntu', 11), justify=CENTER)

#checkbox
login_checked = tk.IntVar()

def login_showpassword():
  if login_checked.get():
    login_epassword.config(show='')
  else:
    login_epassword.config(show='*')

login_checkbox = Checkbutton(login, command=login_showpassword, variable=login_checked, onvalue=1, offvalue=0, cursor='pencil', bg='#DDE6ED')

#add elements to login
login_lheader.place(relx=0.5,y=45,anchor=CENTER)
login_lusername.place(x=30,y=70)
login_eusername.place(relx=0.5,y=106,anchor=CENTER)
login_lpassword.place(x=30,y=130)
login_epassword.place(x=30,y=155)
login_button.place(relx=0.5,y=215,anchor=CENTER)
login_checkbox.place(x=240, y=153)
login_error.place(relx=0.5,y=250,anchor=CENTER)
##################################################

#SIGNUP
##################################################
#labels
signup_lheader = Label(signup, text='SIGN UP', font=('Ubuntu', 20), bg='#DDE6ED')
signup_lusername = Label(signup, text='Username', font=('Ubuntu', 11), bg='#DDE6ED')
signup_lpassword = Label(signup, text='Password', font=('Ubuntu', 11), bg='#DDE6ED')
signup_error = Label(signup, text='', font=('Ubuntu', 9), bg='#DDE6ED', fg='red')

#entries
signup_eusername = ttk.Entry(signup, textvariable=StringVar, font=('Ubuntu', 11), width=29, justify=CENTER)
signup_epassword = ttk.Entry(signup, textvariable=StringVar, font=('Ubuntu', 11), width=25, justify=CENTER, show='*')


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

def check_user():
    if signup_eusername.get() != '':
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
            sign_up()
            
    else:
      signup_error.config(text='Please enter a username')

signup_button = ttk.Button(signup, text='Create account', style='button.TButton', command=check_user, cursor='hand2')

#checkbox
signup_checked = tk.IntVar()

def signup_showpassword():
  if signup_checked.get():
    signup_epassword.config(show='')
  else:
    signup_epassword.config(show='*')

signup_checkbox = Checkbutton(signup, command=signup_showpassword, variable=signup_checked, onvalue=1, offvalue=0, cursor='pencil', bg='#DDE6ED')

#add elements to signup
signup_lheader.place(relx=0.5, y=45, anchor=CENTER)
signup_lusername.place(x=30, y=70)
signup_eusername.place(relx=0.5, y=106, anchor=CENTER)
signup_lpassword.place(x=30, y=130)
signup_epassword.place(x=30, y=155)
signup_button.place(relx=0.5, y=215, anchor=CENTER)
signup_checkbox.place(x=240, y=153)
signup_error.place(relx=0.5, y=250, anchor=CENTER)
##################################################

#MAIN
##################################################
main = Frame(main_frame,  bg='#DDE6ED')
main.pack(fill=BOTH, expand=TRUE)

#buttons
def open_file():
  types = (('Audio files', '*.mp3'), ('All files', '*.*'))
  file = fd.askopenfile(title='Open audio file', filetypes=types)

file_button = ttk.Button(main, text='Open audio file', command=open_file, style='file-button.TButton')
style.configure('file-button.TButton', )

#add elements to main frame
file_button.pack()
##################################################

window.mainloop()