import tkinter as tk

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="login").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="go to signup", command=lambda: master.switch_frame("SignUp")).pack()

if __name__ == "__main__":
    app = Login()
    app.mainloop()