# create.py
# This file holds the account creation window and logic.

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import json
import os
import hashlib


class CreateGUI:
    """A class containing the create account GUI"""

    def __init__(self):
        """Initialize the AccountGUI class."""

        # Create window
        self.win_create = tk.Tk()
        self.win_create.title("Weather Data Analysis | Create Account")
        self.win_create.minsize(width=500, height=250)

        # Configure columns
        self.win_create.columnconfigure(0, minsize=250)
        self.win_create.columnconfigure(1, minsize=250)

        # Configure Rows
        self.win_create.rowconfigure(0, minsize=62.5)
        self.win_create.rowconfigure(1, minsize=62.5)
        self.win_create.rowconfigure(2, minsize=62.5)
        self.win_create.rowconfigure(3, minsize=62.5)

        # Create username widgets.
        self.win_create.lbl_username = tk.Label(self.win_create,
                                                text="Username:",
                                                font=("Helvetica", 10))
        self.win_create.lbl_username.grid(row=0, column=0)

        self.win_create.entry_username = tk.Entry(self.win_create,
                                                  justify="right",
                                                  font=("Helvetica", 10))
        self.win_create.entry_username.grid(row=0, column=1)

        self.win_create.entry_username.focus_force()

        # Create the password widgets.
        self.win_create.lbl_password_guide = tk.Label(self.win_create,
                                                      text="Create a password "
                                                           "of at least nine "
                                                           "(9) characters, "
                                                           "that contains at "
                                                           "least one digit, "
                                                           "one uppercase, "
                                                           "and one lowercase "
                                                           "letter.",
                                                      wraplength=200)
        self.win_create.lbl_password_guide.grid(row=1, column=0, columnspan=2)

        self.win_create.lbl_password = tk.Label(self.win_create,
                                                text="Password:",
                                                font=("Helvetica", 10))
        self.win_create.lbl_password.grid(row=2, column=0)

        self.win_create.entry_password = tk.Entry(self.win_create,
                                                  width=20,
                                                  justify="right",
                                                  show="*")
        self.win_create.entry_password.grid(row=2, column=1)

        self.win_create.btn_create = tk.Button(self.win_create,
                                               text="Create Account",
                                               command=self.create_account)
        self.win_create.btn_create.grid(row=3, column=0)

        self.win_create.btn_cancel = tk.Button(self.win_create,
                                               text="Cancel",
                                               command=self.win_create.destroy)
        self.win_create.btn_cancel.grid(row=3, column=1)

        # Lift to top
        self.win_create.lift()

    def create_account(self):
        """Create a user account."""

        password = self.win_create.entry_password.get()
        username = self.win_create.entry_username.get()

        # If a file does not exist for user accounts, create one with
        # placeholder data.
        if not os.path.isfile("accounts.json"):
            acct_file = open("accounts.json", "w")
            json.dump([{"username": "demo", "password": "Password123"}],
                      acct_file)
            acct_file.close()

        try:
            acct_file = open("accounts.json", "r")
            user_accounts = json.load(acct_file)
        except FileNotFoundError:
            print(f"File {acct_file} does not exist.")

        def validate_username(username):
            """Check to see if the username is taken."""
            if not any(user['username'] == username.lower() for
                       user in user_accounts):
                return True
            else:
                tk.messagebox.showinfo("Invalid Username",
                                       f"The username {username} is already "
                                       f"taken.")

        def validate_password(password):
            """Validate user's password."""
            long_enough = False
            has_lower = False
            has_upper = False
            has_digit = False

            if len(password) >= 9:
                long_enough = True
                for ch in password:
                    if ch.islower():
                        has_lower = True
                    if ch.isupper():
                        has_upper = True
                    if ch.isdigit():
                        has_digit = True

            if long_enough and has_lower and has_upper and has_digit:
                return True
            else:
                tk.messagebox.showinfo("Invalid Password", f"{password} is "
                                                           f"not a valid "
                                                           f"password.")

        if validate_username(username) and validate_password(password):
            hashed_password = hashlib.sha256(str.encode(password)).hexdigest()
            user_accounts.append({'username': username.lower(),
                                  'password': hashed_password})
            tk.messagebox.showinfo("User Account", "Account Creation "
                                                   "Successful!")
            acct_file.close()

            acct_file = open("accounts.json", 'w')
            json.dump(user_accounts, acct_file)
            acct_file.close()
            self.win_create.entry_username.delete(0, END)
            self.win_create.entry_password.delete(0, END)
            self.win_create.destroy()
        else:
            print("Couldn't create account. Please try again.")
            self.win_create.entry_username.delete(0, END)
            self.win_create.entry_password.delete(0, END)
