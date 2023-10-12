import tkinter as tk

from login import Login
from signup import SignUp
from genre import Genre
from charts import Charts

pages = {
    "Login": Login, 
    "SignUp": SignUp,
    "Genre": Genre,
    "Charts": Charts,
}

class MusicApp(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self._frame = None
    self.switch_frame("Charts")

  def switch_frame(self, page_name):
    cls = pages[page_name]
    new_frame = cls(master = self)
    if self._frame is not None:
        self._frame.destroy()
    self._frame = new_frame
    self._frame.pack()

if __name__ == "__main__":
    app = MusicApp()
    app.mainloop()