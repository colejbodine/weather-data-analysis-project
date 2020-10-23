# home.py
# This file holds the Main GUI that accesses the weather station data.

from tkinter import *
import tkinter as tk
import select


class MainGUI:
    """A class holding the login GUI."""

    def __init__(self):
        """Initialize the login GUI."""

        # Create window
        self.win_main = tk.Toplevel()
        self.win_main.title("Weather Data Analysis | Main")
        self.win_main.minsize(width=500, height=250)

        # Configure columns
        self.win_main.columnconfigure(0, minsize=250)
        self.win_main.columnconfigure(1, minsize=250)

        # Configure rows
        self.win_main.rowconfigure(0, minsize=50)
        self.win_main.rowconfigure(1, minsize=50)
        self.win_main.rowconfigure(2, minsize=50)
        self.win_main.rowconfigure(3, minsize=50)

        # Create Main Label
        self.win_main.lbl_main = tk.Label(self.win_main,
                                          text="Weather Data Analysis "
                                               "Interface",
                                          font=("Helvetica", 14))
        self.win_main.lbl_main.grid(row=0, column=0, columnspan=2)

        # Create picture widget
        photo = PhotoImage(file="data_analysis.gif")
        self.labelGIF = tk.Label(self.win_main, image=photo)
        self.labelGIF.image = photo  # Retain a reference
        self.labelGIF.grid(row=1, column=0, columnspan=2)

        # Create Buttons
        self.win_main.btn_1 = tk.Button(self.win_main,
                                        text="Barometric Pressure and "
                                             "Temperature",
                                        width=30,
                                        command=self.open_selection_gui)
        self.win_main.btn_1.grid(row=2, column=0)

        self.win_main.btn_2 = tk.Button(self.win_main,
                                        text="Barometric Pressure and Wind "
                                             "Speed",
                                        width=30,
                                        command=self.open_selection_gui)
        self.win_main.btn_2.grid(row=2, column=1)

        self.win_main.btn_3 = tk.Button(self.win_main,
                                        text="Barometric Pressure and Sky "
                                             "Cover",
                                        width=30,
                                        command=self.open_selection_gui)
        self.win_main.btn_3.grid(row=3, column=0)

        self.win_main.btn_4 = tk.Button(self.win_main,
                                        text="Temperature and Dew Point",
                                        width=30,
                                        command=self.open_selection_gui)
        self.win_main.btn_4.grid(row=3, column=1)

    def open_selection_gui(self):
        """This function opens up the selection gui."""
        self.select_GUI = select.SelectGUI()