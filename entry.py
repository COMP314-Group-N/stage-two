#GUI imports
import tkinter as tk
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk

#screen imports
from login import login_frame
from signup import signup_frame
from main import main_frame

#creates window======
window = tk.Tk()
style = Style(theme='superhero')
window.title('Music Identification')
window.resizable(False, False)
#====================

#center window=======
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
 
x = (screen_width/2) - (525/2)
y = (screen_height/2) - (400/2)
 
window.geometry('%dx%d+%d+%d' % (525, 400, x, y))
#====================

#creates frames for each screen
start_frame = ttk.Frame(window)
main = main_frame(window, start_frame, screen_height, screen_width)
#====================

main.pack(fill=BOTH, expand=True)

#creates tab interface
tabs = ttk.Notebook(start_frame)
style.configure('TNotebook', padding=5)
style.configure('TNotebook.Tab', font=('Leelawadee', 10))
tabs.pack(fill=BOTH, expand=True)
#====================

#create a tab for each screen
login = login_frame(tabs, window, start_frame, main, screen_height, screen_width)
signup = signup_frame(tabs, window, start_frame, main, screen_height, screen_width)
#====================

#add screen tabs to tab interface
tabs.add(login, text='Login')
tabs.add(signup, text='Sign up')
#====================

window.mainloop()