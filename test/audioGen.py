import tkinter as tk

class AudioGen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="audio gen").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to page two", command=lambda: master.switch_frame("PageTwo")).pack()

if __name__ == "__main__":
    app = AudioGen()
    app.mainloop()