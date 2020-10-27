# select_bp_t.py
# This file allows the user to select from the range of dates what they would
# like to view and prints information about barometric pressure and temperature.

import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import datetime


class SelectBPTGUI:
    """This class holds the window for selecting a date range."""

    def __init__(self):
        """Initialize the GUI"""

        # Create variables
        self.filename = 'Data_2010_thru_2018.txt'
        self.dates = []

        # Read in the file and append each date to dates
        with open(self.filename, 'r') as f:
            next(f)
            for line in f:
                self.date = line[0:4] + " " + line[4:6] + " " + line[6:8] + " " \
                            + line[8:10] + ":" + line[10:12]
                self.dates.append(self.date)

        # Create the window
        self.win_select = tk.Tk()
        self.win_select.title("Weather Data Analysis | BP and Temperature")
        self.win_select.minsize(width=500, height=250)

        # Configure columns
        self.win_select.columnconfigure(0, minsize=150)
        self.win_select.columnconfigure(1, minsize=150)
        self.win_select.columnconfigure(2, minsize=150)

        # Configure rows
        self.win_select.rowconfigure(0, minsize=75)
        self.win_select.rowconfigure(1, minsize=75)
        self.win_select.rowconfigure(2, minsize=75)
        self.win_select.rowconfigure(3, minsize=75)

        # Create main label
        self.lbl_main = tk.Label(self.win_select,
                                 text="Weather Data Analysis",
                                 font=("Arial", 16))
        self.lbl_main.grid(row=0, column=1)

        # Create description label
        self.lbl_desc = tk.Label(self.win_select,
                                 text="Select a range of dates (YYYY MM DD):",
                                 font=("Arial", 12))
        self.lbl_desc.grid(row=1, column=1)

        # Create first OptionMenu.
        self.opt1 = ttk.Combobox(self.win_select, values=self.dates)
        self.opt1.config(font=('Helvetica', 12))
        self.opt1.grid(row=2, column=0)

        # Create middle label.
        self.lbl_to = tk.Label(self.win_select,
                               text="to",
                               font=("Arial", 12))
        self.lbl_to.grid(row=2, column=1)

        # Create second OptionMenu.
        self.opt2 = ttk.Combobox(self.win_select, values=self.dates)
        self.opt2.config(font=('Helvetica', 12))
        self.opt2.grid(row=2, column=2)

        # Create select button
        self.btn_select = tk.Button(self.win_select,
                                    text="Select",
                                    font=("Arial", 12),
                                    command=self.get_values)
        self.btn_select.grid(row=3, column=1)

    def get_values(self):
        # Create variables
        self.filename = 'Data_2010_thru_2018.txt'
        self.file = open(self.filename, 'r')
        self.lines = self.file.readlines()
        val1 = self.opt1.get()
        val2 = self.opt2.get()
        ind1 = self.opt1.current()
        ind2 = self.opt2.current()
        bps = []
        ts = []
        dates = []

        # Gather range for data
        self.lines = self.lines[(ind1 + 1):ind2]

        # Store bp, temp and date
        for line in self.lines:
            bp = line.split(' ')[23]
            t = line.split(' ')[22]
            date = datetime.datetime(int(line[0:4]), int(line[4:6]),
                                     int(line[6:8]), int(line[8:10]),
                                     int(line[10:12]))
            # Ignore invalid variables and append valid ones to correct lists.
            if '*' not in bp and '*' not in t:
                dates.append(date)
                bps.append(getdouble(bp))
                ts.append(getdouble(t))

        # Create plot variables
        x = np.array(dates)
        print(x)
        y1 = np.array(bps)
        print(y1)
        y2 = np.array(ts)
        print(y2)

        fig, ax1 = plt.subplots()

        # Create a second y-axis along the same x-axis
        ax2 = ax1.twinx()

        # Plot axes
        ax2 = ax1.twinx()
        ax1.plot(x, y1, 'g-', label="Barometric Pressure")
        ax2.plot(x, y2, 'b-', label="Temperature")

        # Set labels
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Barometric Pressure", color='g')
        ax2.set_ylabel("Temperature", color='b')

        # Create plot
        plt.title(f"Barometric Pressure vs Temperature from {val1} to {val2}")
        plt.show()
