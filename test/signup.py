import tkinter as tk

class SignUp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="signup").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="go to login", command=lambda: master.switch_frame("Login")).pack()

if __name__ == "__main__":
    app = SignUp()
    app.mainloop()