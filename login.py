# login.py
# This login window and logic.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import hashlib
import main


class LoginGUI:
    """A class holding the login GUI."""

    def __init__(self):
        """Initialize the login GUI."""

        # Create window
        self.win_login = tk.Tk()
        self.win_login.title("Weather Data Analysis | Log In")
        self.win_login.minsize(width=500, height=250)

        # Configure columns
        self.win_login.columnconfigure(0, minsize=250)
        self.win_login.columnconfigure(1, minsize=250)

        # Configure Rows
        self.win_login.rowconfigure(0, minsize=62.5)
        self.win_login.rowconfigure(1, minsize=62.5)
        self.win_login.rowconfigure(2, minsize=62.5)
        self.win_login.rowconfigure(3, minsize=62.5)

        # Create Login Label
        self.win_login.lbl_title = tk.Label(self.win_login,
                                            text="Log In",
                                            font=("Arial", 16))
        self.win_login.lbl_title.grid(row=0, column=0, columnspan=2)

        # Create username widgets.
        self.win_login.lbl_username = tk.Label(self.win_login,
                                               text="Username:",
                                               font=("Helvetica", 10))
        self.win_login.lbl_username.grid(row=1, column=0)

        self.win_login.entry_username = tk.Entry(self.win_login,
                                                 justify="right",
                                                 font=("Helvetica", 10))
        self.win_login.entry_username.grid(row=1, column=1)

        self.win_login.entry_username.focus_force()

        # Create the password widgets.

        self.win_login.lbl_password = tk.Label(self.win_login,
                                               text="Password:",
                                               font=("Helvetica", 10))
        self.win_login.lbl_password.grid(row=2, column=0)

        self.win_login.entry_password = tk.Entry(self.win_login,
                                                 width=20,
                                                 justify="right",
                                                 show="*")
        self.win_login.entry_password.grid(row=2, column=1)

        self.win_login.btn_create = tk.Button(self.win_login,
                                              text="Log In",
                                              command=self.log_in)
        self.win_login.btn_create.grid(row=3, column=0)

        self.win_login.btn_cancel = tk.Button(self.win_login,
                                              text="Cancel",
                                              command=self.win_login.destroy)
        self.win_login.btn_cancel.grid(row=3, column=1)

        # Lift to top
        self.win_login.lift()

    def log_in(self):
        """Log the user in."""
        username = self.win_login.entry_username.get()
        password = self.win_login.entry_password.get()
        hashed_password = hashlib.sha256(str.encode(password)).hexdigest()
        # Try to open the file
        try:
            acct_file = open("accounts.json", "r")
            user_accounts = json.load(acct_file)
        except IOError:
            tk.messagebox.showinfo("FILE ERROR", f"File {acct_file} does not "
                                                 f"exist.")

        if any(user['username'] == username.lower() and
               user['password'] == hashed_password for user in user_accounts):
            self.main_GUI = main.MainGUI()
            self.win_login.destroy()

        if not any(user['username'] == username.lower() for
                   user in user_accounts):
            tk.messagebox.showinfo("Log In", f"User {username} does not exist.")
            self.win_login.entry_username.delete(0, END)
            self.win_login.entry_password.delete(0, END)
        elif any(user['username'] == username.lower() and
                 not user['password'] == hashed_password for
                 user in user_accounts):
            tk.messagebox.showinfo("Log In", "Invalid password.")
            self.win_login.entry_username.delete(0, END)
            self.win_login.entry_password.delete(0, END)
