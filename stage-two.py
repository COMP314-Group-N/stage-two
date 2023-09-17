#GUI imports
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk
import librosa as lib

#functional imports
import csv
from statemachine import StateMachine as sm, State

#WINDOW
##################################################
#creates window
window = tk.Tk()
style = Style(theme='superhero')
window.title('Music Identification')
window.resizable(False, False)

#center window
#**************************************************
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
 
x = (screen_width/2) - (750/2)
y = (screen_height/2) - (400/2)
 
window.geometry('%dx%d+%d+%d' % (750, 400, x, y))
#**************************************************

#creates frames for each screen
start_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

#**************************************************
main_frame.pack(fill=BOTH, expand=True)
#**************************************************

#creates tab interface
tabs = ttk.Notebook(start_frame)
style.configure('TNotebook', padding=5)
style.configure('TNotebook.Tab', font=('Leelawadee', 10))
tabs.pack(fill=BOTH, expand=True)

#create a tab for each screen
login = Frame(tabs)
signup = Frame(tabs)

#add screen tabs to tab interface
tabs.add(login, text='Login')
tabs.add(signup, text='Sign up')
##################################################

#LOGIN
##################################################
#labels
login_lheader = ttk.Label(login, text='LOGIN', font=('Leelawadee', 20))
login_lusername = ttk.Label(login, text='Username', font=('Leelawadee', 11))
login_lpassword = ttk.Label(login, text='Password', font=('Leelawadee', 11))
login_error = ttk.Label(login, text='', font=('Leelawadee', 9), style='danger.TLabel', justify=CENTER)

#entries
login_eusername = ttk.Entry(login, textvariable=StringVar, font=('Leelawadee', 11), width=29, justify=CENTER, style='primary.TEntry')
login_epassword = ttk.Entry(login, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry', show='*')

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

login_button = ttk.Button(login, text='Log in', style='primary.Outline.TButton', command=check_login, cursor='hand2')

style.configure('primary.Outline.TButton', font=('Leelawadee', 11), justify=CENTER)

#checkbox
login_checked = tk.IntVar()

def login_showpassword():
  if login_checked.get():
    login_epassword.config(show='')
  else:
    login_epassword.config(show='*')

login_checkbox = ttk.Checkbutton(login, command=login_showpassword, variable=login_checked, onvalue=1, offvalue=0, cursor='hand2', style='primary.Squaretoggle.Toolbutton')

#add elements to login
login_lheader.place(relx=0.5,y=35,anchor=CENTER)
login_lusername.place(x=30,y=68)
login_eusername.place(relx=0.5,y=106,anchor=CENTER)
login_lpassword.place(x=30,y=138)
login_epassword.place(relx=0.45,y=176, anchor=CENTER)
login_button.place(relx=0.5,y=230,anchor=CENTER)
login_checkbox.place(relx=0.875,y=176,anchor=CENTER)
login_error.place(relx=0.5,y=270,anchor=CENTER)
##################################################

#SIGNUP
##################################################
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
##################################################

#MAIN
##################################################
main = Frame(main_frame,highlightbackground='#526170',highlightthickness=1)
main.pack(padx=5,pady=5,fill=BOTH,expand=True)

#Audio
def process_audio(file):
  audio_file = lib.load(file)
  y, sr = audio_file
  tempo, beat_frames = lib.beat.beat_track(y=y,sr=sr)
  main_ebeats.insert(0,'{:.2f} BPM'.format(tempo))

#FSM


#labels
main_header = ttk.Label(main, text='GENRE CLASSIFICATION', font=('Leelawadee', 20))
main_lbeats = ttk.Label(main, text='Estimated beats per minute', font=('Leelawadee', 11))

#entries
main_ebeats = ttk.Entry(main, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry')

#buttons
def logout():
  x = (screen_width/2) - (310/2)
  y = (screen_height/2) - (340/2)
  window.geometry('%dx%d+%d+%d' % (310, 340, x, y))
  main_frame.pack_forget()
  start_frame.pack(fill=BOTH, expand=True)

logout_button = ttk.Button(main, text='Log out', command=logout, style='danger.Outline.TButton', cursor='hand2')
style.configure('danger.Outline.TButton', font=('Leelawadee', 11), justify=CENTER)

def open_file():
  types = (('Audio files', ['*.mp3', '*.wav']), ('All files', '*.*'))
  file = fd.askopenfilename(title='Open audio file', filetypes=types)
  if file != '':
    process_audio(file)

file_button = ttk.Button(main, text='Open audio file', command=open_file, style='primary.Outline.TButton', cursor='hand2')

#add elements to main frame
main_header.place(relx=0.5,y=35,anchor=CENTER)
main_lbeats.place(relx=0.165,y=78,anchor=CENTER)
main_ebeats.place(relx=0.18,y=106,anchor=CENTER)
file_button.place(relx=0.11,y=355,anchor=CENTER)
logout_button.place(relx=0.925,y=355,anchor=CENTER)

##################################################

window.mainloop()