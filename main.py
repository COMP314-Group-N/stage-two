import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

import librosa as lib
from statemachine import StateMachine as sm, State

def main_frame(window, start_frame, screen_height, screen_width):
  main = Frame(window)
  main_inner = Frame(main, highlightbackground='#526170', highlightthickness=1)
  main_inner.pack(padx=5,pady=5,fill=BOTH,expand=True)
  style = Style(theme='superhero')

  #Audio
  def process_audio(file):
    audio_file = lib.load(file)
    y, sr = audio_file
    tempo, beat_frames = lib.beat.beat_track(y=y,sr=sr)
    main_ebeats.delete(0, END)
    main_ebeats.insert(0,'{:.2f} BPM'.format(tempo))

  #FSM


  #labels
  main_header = ttk.Label(main_inner, text='GENRE CLASSIFICATION', font=('Leelawadee', 20))
  main_lbeats = ttk.Label(main_inner, text='Estimated beats per minute', font=('Leelawadee', 11))

  #entries
  main_ebeats = ttk.Entry(main_inner, textvariable=StringVar, font=('Leelawadee', 11), width=25, justify=CENTER, style='primary.TEntry')

  #buttons
  def logout():
    x = (screen_width/2) - (310/2)
    y = (screen_height/2) - (340/2)
    window.geometry('%dx%d+%d+%d' % (310, 340, x, y))
    main.pack_forget()
    start_frame.pack(fill=BOTH, expand=True)

  logout_button = ttk.Button(main_inner, text='Log out', command=logout, style='danger.Outline.TButton', cursor='hand2')
  style.configure('danger.Outline.TButton', font=('Leelawadee', 11), justify=CENTER)

  def open_file():
    types = (('Audio files', ['*.mp3', '*.wav']), ('All files', '*.*'))
    file = fd.askopenfilename(title='Open audio file', filetypes=types)
    if file != '':
      process_audio(file)

  file_button = ttk.Button(main_inner, text='Open audio file', command=open_file, style='primary.Outline.TButton', cursor='hand2')

  #add elements to main frame
  main_header.place(relx=0.5,y=35,anchor=CENTER)
  main_lbeats.place(relx=0.165,y=78,anchor=CENTER)
  main_ebeats.place(relx=0.18,y=106,anchor=CENTER)
  file_button.place(relx=0.11,y=355,anchor=CENTER)
  logout_button.place(relx=0.925,y=355,anchor=CENTER)

  return main