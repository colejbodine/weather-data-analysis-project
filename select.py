# select.py
# This file allows the user to select from the range of dates what they would
# like to view.

from tkinter import *
import tkinter as tk


class SelectGUI:
    """This class holds the window for selecting a date range."""

    def __init__(self):
        """Initialize the login GUI."""

        # Create window
        self.win_main = tk.Toplevel()
        self.win_main.title("Weather Data Analysis | Select Date(s)")
        self.win_main.minsize(width=500, height=250)
