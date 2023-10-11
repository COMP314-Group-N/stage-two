import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from ttkbootstrap import Style
from tkinter import ttk

import librosa as lib
import librosa.display

class Genre(tk.Frame):
  def __init__(self, master):
    master.title('Login')
    master.resizable(False, False)
    
    Frame.__init__(self, master)
    self.config(highlightthickness=1, highlightbackground='#7F8B96')
    style = Style(theme='superhero')

    w = master.winfo_screenwidth()
    h = master.winfo_screenheight()
    x = (w/2) - (525/2)
    y = (h/2) - (390/2)
    master.geometry('%dx%d+%d+%d' % (525, 390, x, y))
    self.pack(fill=BOTH, expand=True, padx=5, pady=5)

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
      ebeats.delete(0, END)
      beatText.set('{:.2f} BPM'.format(tempo))
      ttempo.delete('1.0', END)
      ttempo.insert(INSERT, beat_frames)
      ttempo.config(state=DISABLED)  
      song_genre_fsm = GenreFSM()
      genre = song_genre_fsm.determine_genre(file)
      current_genre = song_genre_fsm.get_current_genre()
      
      detText.set(genre)
      curText.set(current_genre)
    #====================

    #labels==============
    header = ttk.Label(self, text='GENRE CLASSIFICATION', font=('Leelawadee', 20))
    lselected = ttk.Label(self, text='Selected audio file', font=('Leelawadee', 11))
    lbeats = ttk.Label(self, text='Estimated beats per minute', font=('Leelawadee', 11))
    ltempo = ttk.Label(self, text='Beat frames', font=('Leelawadee', 11))
    lcurrent = ttk.Label(self, text='Current genre', font=('Leelawadee', 11))
    lgenre = ttk.Label(self, text='Determined genre', font=('Leelawadee', 11))
    #====================

    #entries=============
    beatText = StringVar()
    selText = StringVar()
    curText = StringVar()
    detText = StringVar()
    ebeats = ttk.Entry(self, textvariable=beatText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
    eselected = ttk.Entry(self, textvariable=selText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
    ecurrent = ttk.Entry(self, textvariable=curText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
    egenre = ttk.Entry(self, textvariable=detText, state='readonly', font=('Leelawadee', 11), style='primary', width=25)
    #====================

    #texts===============
    ttempo = Text(self, height=2, width=55, font=('Leelawadee', 11), yscrollcommand=set())
    #====================

    #buttons=============
    blogout = ttk.Button(self, text='Log out', style='danger.Outline.TButton', cursor='hand2', command=lambda: master.switch_frame('Login'))

    def open_file():
      ttempo.config(state=NORMAL)
      types = (('Audio files', ['*.mp3', '*.wav']), ('All files', '*.*'))
      file = fd.askopenfilename(title='Open audio file', filetypes=types)
      if file != '':
        process_audio(file)

    bfile = ttk.Button(self, text='Open audio file', command=open_file, style='primary.Outline.TButton', cursor='hand2')

    bcharts = ttk.Button(self, text='View charts', style='primary.Outline.TButton', cursor='hand2', command=lambda: master.switch_frame('Charts'))
    #====================

    #add elements to frame
    header.place(relx=.5, y=45, anchor=CENTER)
    lselected.place(relx=.06, y=98, anchor=W)
    eselected.place(relx=.055, y=126, anchor=W)
    lbeats.place(relx=.53, y=98, anchor=W)
    ebeats.place(relx=.525, y=126, anchor=W)
    ltempo.place(relx=.06, y=170, anchor=W)
    ttempo.place(relx=.055, y=208, anchor=W)
    lcurrent.place(relx=.06, y=260, anchor=W)
    ecurrent.place(relx=.055, y=288, anchor=W)
    lgenre.place(relx=.53, y=260, anchor=W)
    egenre.place(relx=.525, y=288, anchor=W)
    bfile.place(relx=.055, y=340, anchor=W)
    blogout.place(relx=.815, y=340, anchor=W)
    bcharts.place(relx=.625, y=340, anchor=W)
    #====================

if __name__ == "__main__":
    app = Genre()
    app.mainloop()