import tkinter as tk
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk

from tinydb import TinyDB, Query

db = TinyDB('charts.json')
gquery = Query()
squery = Query()

class Charts(tk.Frame):
  def __init__(self, master):
    master.title('Charts')

    Frame.__init__(self, master)
    self.config(highlightthickness=1, highlightbackground='#7F8B96')
    style = Style(theme='superhero')

    w = master.winfo_screenwidth()
    h = master.winfo_screenheight()
    x = (w/2) - (525/2)
    y = (h/2) - (390/2)
    master.geometry('%dx%d+%d+%d' % (525, 390, x, y))
    self.pack(fill=BOTH, expand=True, padx=5, pady=5)

    #labels==============
    header = ttk.Label(self, text='MUSIC CHARTS', font=('Leelawadee', 20))
    lgenres = ttk.Label(self, text='Select a genre', font=('Leelawadee', 11))
    lsongs = ttk.Label(self, text='Top 10 songs', font=('Leelawadee', 11))
    #====================

    #treeview============
    tsongs = ttk.Treeview(self, columns=('number', 'title', 'artist'), show='headings')
    tsongs.heading('number', text='No.')
    tsongs.heading('title', text='Title')
    tsongs.heading('artist', text='Artist')
    #====================

    #listbox=============
    genres = ('Country', 'Dubstep', 'Hip-Hop', 'Jazz', 'Pop', 'Rock', 'R&B')
    var = Variable(value=genres)

    def show_songs(event):
      genre = listgenres.get(listgenres.curselection())
      print(genre)
      print(db.search(gquery.genre == genre))


    listgenres = Listbox(self, listvariable=var, selectmode=SINGLE, font=('Leelawadee', 11), height=7, width=13, cursor='hand2')
    listgenres.bind('<<ListboxSelect>>', show_songs)
    #====================

    #buttons=============
    blogout = ttk.Button(self, text='Log out', style='danger.Outline.TButton', cursor='hand2', command=lambda: master.switch_frame('Login'))

    bgenre = ttk.Button(self, text='Genre classification', style='primary.Outline.TButton', cursor='hand2', command=lambda: master.switch_frame('Genre'))
    #====================

    #add elements to frame
    header.place(relx=.5, y=45, anchor=CENTER)
    lgenres.place(relx=.06, y=98, anchor=W)
    listgenres.place(relx=.055, y=176, anchor=W)
    lsongs.place(relx=.53, y=98, anchor=W)
    bgenre.place(relx=.055, y=340, anchor=W)
    blogout.place(relx=.815, y=340, anchor=W)
    #====================

if __name__ == "__main__":
  app = Charts()
  app.mainloop()