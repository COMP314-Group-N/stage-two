import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

import librosa as lib
import librosa.display

def main_frame(window, start_frame, screen_height, screen_width):
  main = Frame(window)
  main_inner = Frame(main, highlightbackground='#526170', highlightthickness=1)
  main_inner.pack(padx=5,pady=5,fill=BOTH,expand=True)
  style = Style(theme='superhero')

  #FSM=================
  class GenreFSM:
    def __init__(self):
      self.states = {
        'Blues': (60, 80),
        'Dubstep': (140, 160),
        'Hip-Hop': (80, 115),
        'Jazz/Country': (90, 120),
        'Pop': (90, 130),
        'Rock': (160, 220),
        'R&B': (70, 90),  
      }
        
      self.transitions = {
        'Blues': ['Dubstep','Hip-Hop','Jazz/Country','Pop','Rock','R&B'],
        'Dubstep': ['Blues','Hip-Hop','Jazz/Country','Pop','Rock','R&B'],
        'Hip Hop': ['Blues','Dubstep','Jazz/Country','Pop','Rock','R&B'],
        'Jazz/Country': ['Blues','Dubstep','Hip-Hop','Pop','Rock','R&B'],
        'Pop': ['Blues','Dubstep','Hip-Hop','Jazz/Country','Rock','R&B'],
        'Rock': ['Blues','Dubstep','Hip-Hop','Jazz/Country','Pop','R&B'],
        'R&B': ['Blues','Dubstep','Hip-Hop','Jazz/Country','Pop','Rock'],
      }
        
      self.current_state = 'Unknown'
        
    def determine_genre(self, audio_file):
      y, sr = librosa.load(audio_file)
      onset_env = librosa.onset.onset_strength(y=y, sr=sr)
      tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
        
      matching_genre = None
      for genre, (min_bpm, max_bpm) in self.states.items():
        if min_bpm <= tempo <= max_bpm:
          matching_genre = genre
          break
        
      if matching_genre:
        self.transition_genre(matching_genre)
        return matching_genre
      else:
        print(f"No matching genre found for tempo {tempo}.")
        return 'Unknown'
    
    def transition_genre(self, genre):
      if genre in self.transitions.get(self.current_state, []):
        self.current_state = genre
      else:
        print(f"Cannot transition from {self.current_state} to {genre}.")
    
    def get_current_genre(self):
      return self.current_state
  #====================

  #Audio===============
  def process_audio(file):
    audio_file = lib.load(file)
    selText.set('\'' + file.rsplit('/', 1)[1] + '\'')
    y, sr = audio_file
    tempo, beat_frames = lib.beat.beat_track(y=y,sr=sr)
    main_ebeats.delete(0, END)
    beatText.set('{:.2f} BPM'.format(tempo))
    #beat_frames = lib.frames_to_time(beat_frames, sr=sr)
    main_ttempo.delete('1.0', END)
    main_ttempo.insert(INSERT, beat_frames)
    main_ttempo.config(state=DISABLED)

    song_genre_fsm = GenreFSM()
    genre = song_genre_fsm.determine_genre(file)
    current_genre = song_genre_fsm.get_current_genre()
    
    detText.set(genre)
    curText.set(current_genre)
    print(f"Audio File: {file} => Genre: {genre}")
    print(f"Current Genre: {current_genre}\n")
  #====================

  #labels==============
  main_header = ttk.Label(main_inner, text='GENRE CLASSIFICATION', font=('Leelawadee', 20))
  main_lselected = ttk.Label(main_inner, text='Selected audio file', font=('Leelawadee', 11))
  main_lbeats = ttk.Label(main_inner, text='Estimated beats per minute', font=('Leelawadee', 11))
  main_ltempo = ttk.Label(main_inner, text='Beat frames', font=('Leelawadee', 11))
  main_lcurrent = ttk.Label(main_inner, text='Current genre', font=('Leelawadee', 11))
  main_lgenre = ttk.Label(main_inner, text='Determined genre', font=('Leelawadee', 11))
  #====================

  #entries=============
  beatText = StringVar()
  selText = StringVar()
  curText = StringVar()
  detText = StringVar()
  main_ebeats = ttk.Entry(main_inner, textvariable=beatText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
  main_eselected = ttk.Entry(main_inner, textvariable=selText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
  main_ecurrent = ttk.Entry(main_inner, textvariable=curText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
  main_egenre = ttk.Entry(main_inner, textvariable=detText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
  #====================

  #texts===============
  main_ttempo = Text(main_inner, height=2, width=57, font=('Leelawadee', 11), yscrollcommand=set())
  #====================

  #buttons=============
  def logout():
    x = (screen_width/2) - (310/2)
    y = (screen_height/2) - (340/2)
    window.geometry('%dx%d+%d+%d' % (310, 340, x, y))
    main.pack_forget()
    start_frame.pack(fill=BOTH, expand=True)

  logout_button = ttk.Button(main_inner, text='Log out', command=logout, style='danger.Outline.TButton', cursor='hand2')
  style.configure('danger.Outline.TButton', font=('Leelawadee', 11), justify=CENTER)

  def open_file():
    main_ttempo.config(state=NORMAL)
    types = (('Audio files', ['*.mp3', '*.wav']), ('All files', '*.*'))
    file = fd.askopenfilename(title='Open audio file', filetypes=types)
    if file != '':
      process_audio(file)

  file_button = ttk.Button(main_inner, text='Open audio file', command=open_file, style='primary.Outline.TButton', cursor='hand2')
  #====================

  #add elements to main frame
  main_header.place(relx=0.5,y=45,anchor=CENTER)
  main_lselected.place(relx=.0425,y=98,anchor=W)
  main_eselected.place(relx=.0425,y=126,anchor=W)
  main_lbeats.place(relx=.54,y=98,anchor=W)
  main_ebeats.place(relx=.54,y=126,anchor=W)
  main_ltempo.place(relx=.0425,y=170,anchor=W)
  main_ttempo.place(relx=.0425,y=208,anchor=W)
  main_lcurrent.place(relx=.0425,y=260,anchor=W)
  main_ecurrent.place(relx=.0425,y=288,anchor=W)
  main_lgenre.place(relx=.54,y=260,anchor=W)
  main_egenre.place(relx=.54,y=288,anchor=W)
  file_button.place(relx=.0425,y=350,anchor=W)
  logout_button.place(relx=.815,y=350,anchor=W)
  #====================

  return main