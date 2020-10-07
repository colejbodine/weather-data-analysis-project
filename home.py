# home.py
# This file stores the home window for the weather data analysis project.

from tkinter import *
import tkinter as tk
import create
import login
import main

# home window
class HomeGUI:
    """A class holding the home window."""

    def __init__(self):
        """Initialize the home window."""

        # Create the home window.
        self.win_home = tk.Tk()
        self.win_home.title("Weather Data Analysis | Home")
        self.win_home.minsize(width=450, height=300)

        # Configure columns
        self.win_home.columnconfigure(0, minsize=150)
        self.win_home.columnconfigure(1, minsize=150)
        self.win_home.columnconfigure(2, minsize=150)

        # Configure Rows
        self.win_home.rowconfigure(0, minsize=50)
        self.win_home.rowconfigure(1, minsize=50)
        self.win_home.rowconfigure(2, minsize=50)
        self.win_home.rowconfigure(3, minsize=50)
        self.win_home.rowconfigure(4, minsize=50)
        self.win_home.rowconfigure(5, minsize=50)

        # Create label widget.
        self.lbl_header = tk.Label(text="Weather Data Analysis Program",
                                   font=("Helvetica", 16),
                                   fg="blue")

        self.lbl_header.grid(row=1, column=0, columnspan=3)

        # Create the picture widget.
        photo = PhotoImage(file="weather.gif")
        self.labelGIF = tk.Label(image=photo)
        self.labelGIF.image = photo
        self.labelGIF.grid(row=3, column=1)

        # Create the button widgets.
        self.btn_login = tk.Button(text="Log In",
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
                                  command=self.win_home.destroy)

        self.btn_login.grid(row=5, column=0)
        self.btn_create_acct.grid(row=5, column=1)
        self.btn_quit.grid(row=5, column=2)

        # Enter home tkinter loop
        tk.mainloop()

    def create_account(self):
        # Disable the buttons
        self.btn_create_acct.config(state=DISABLED)
        self.btn_login.config(state=DISABLED)

        # Create an account creation GUI
        self.acct_GUI = create.CreateGUI()

        # Wait for the window to be destroyed.
        self.acct_GUI.win_create.wait_window()

        # Enable login button again.
        self.btn_login.config(state=NORMAL)
        self.btn_create_acct.config(state=NORMAL)

    def log_in(self):
        # Disable the buttons
        self.btn_create_acct.config(state=DISABLED)
        self.btn_login.config(state=DISABLED)

        # Create an account creation GUI
        self.login_GUI = login.LoginGUI()

        # Wait for the windows  to be destroyed.
        self.login_GUI.win_login.wait_window()

        # Enable login and create buttons again.
        self.btn_login.config(state=NORMAL)
        self.btn_create_acct.config(state=NORMAL)



dataProgram = HomeGUI()

################################################################################
