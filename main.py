# main.py
# This file stores the main window for the weather data analysis project.

from tkinter import *
import tkinter as tk
import create
import login


# main window
class MainGUI:
    """A class holding the main window."""

    def __init__(self):
        """Initialize the main window."""

        # Create the main window.
        self.win_main = tk.Tk()
        self.win_main.title("Weather Data Analysis | Home")
        self.win_main.minsize(width=450, height=300)

        # Configure columns
        self.win_main.columnconfigure(0, minsize=150)
        self.win_main.columnconfigure(1, minsize=150)
        self.win_main.columnconfigure(2, minsize=150)

        # Configure Rows
        self.win_main.rowconfigure(0, minsize=50)
        self.win_main.rowconfigure(1, minsize=50)
        self.win_main.rowconfigure(2, minsize=50)
        self.win_main.rowconfigure(3, minsize=50)
        self.win_main.rowconfigure(4, minsize=50)
        self.win_main.rowconfigure(5, minsize=50)

        # Create label widget.
        self.lbl_header = tk.Label(text="Weather Data Analysis Program",
                                   font=("Helvetica", 16),
                                   fg="blue")

        self.lbl_header.grid(row=1, column=0, columnspan=3)

        # Create the picture widget.
        photo = PhotoImage(file="weather.gif")
        self.labelGIF = tk.Label(image=photo)
        self.labelGIF.image = photo  # retain a reference
        self.labelGIF.grid(row=3, column=1)

        # Create the button widgets.
        self.btn_login = tk.Button(text="Login",
                                   font=("Helvetica", 10),
                                   width=16,
                                   command=self.log_in)

        self.btn_create_acct = tk.Button(text="Create Account",
                                         font=("Helvetica", 10),
                                         width=16,
                                         command=self.create_account)

        self.btn_quit = tk.Button(text="Cancel",
                                  font=("Helvetica", 10),
                                  width=16,
                                  command=self.win_main.destroy)

        self.btn_login.grid(row=5, column=0)
        self.btn_create_acct.grid(row=5, column=1)
        self.btn_quit.grid(row=5, column=2)

        # Enter main tkinter loop
        tk.mainloop()

    def create_account(self):
        # Disable the buttons
        self.btn_create_acct.config(state=DISABLED)
        self.btn_login.config(state=DISABLED)

        # Create an account creation GUI
        self.acct_GUI = create.AccountGUI()

        # Wait for the window to be destroyed.
        self.acct_GUI.win_create.wait_window()

        # Enable login button again.
        self.btn_login.config(state=NORMAL)

    def log_in(self):
        # Disable the buttons
        self.btn_create_acct.config(state=DISABLED)
        self.btn_login.config(state=DISABLED)

        # Create an account creation GUI
        self.login_GUI = login.LoginGUI()

        # Wait for the window to be destroyed.
        self.login_GUI.win_login.wait_window()

        # Enable login and create buttons again.
        self.btn_login.config(state=NORMAL)
        self.btn_create_acct.config(state=NORMAL)


dataProgram = MainGUI()
