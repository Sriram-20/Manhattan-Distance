# This is responsible for creeating the GUI

from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class View:

    # This method creates creates the window, widgets, and adds all the widgets to the windwow
    def __init__(self, controller):
        # Create main window and give it a title
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("Manhattan Distance")

        # Create frame to put inside window (our content will be placed inside this frame)
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.pack(expand=True)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Create all necessary widgets (this is our content that will be displayed)
        # self.problem_description: Text label that explains the Manhattan distance
        # self.user_instructions: Text label that tells the user how to enter values
        self.problem_description = ttk.Label(self.mainframe, wraplength=400, text="The Manhattan distance is the distance between two points in a grid (like the grid-like street geography of the New York borough of Manhattan) calculated by only taking a vertical and/or horizontal path.")
        self.user_instructions = ttk.Label(self.mainframe, wraplength=400, text="Please enter two points below. \nNote: Value entered must be integers.")
        # Point A widgets
        # self.pointA_label: "Point A"
        # self.pointA_x_label: "x-coordinate"
        # self.PointA_y_label: "y-coordinate"
        # self.pointA_x_input: Input box for Point A x-coordinate
        # self.pointA_y_input: Input box for Point A y-coordinate
        self.pointA_label = ttk.Label(self.mainframe, text="Point A")
        self.pointA_x_label = ttk.Label(self.mainframe, text="x-coordinate:")
        self.pointA_y_label = ttk.Label(self.mainframe, text="y-coordinate:")
        self.pointA_x_input = ttk.Entry(self.mainframe)
        self.pointA_y_input = ttk.Entry(self.mainframe)    
        # Point B widgets
        # self.pointB_label: "Point B"
        # self.pointB_x_label: "x-coordinate"
        # self.pointB_y_label: "y-coordinate"
        # self.pointB_x_input: Input box for Point B x-coordinate
        # self.pointB_y_input: Input box for Point B y-coordinate
        self.pointB_label = ttk.Label(self.mainframe, text="Point B")
        self.pointB_x_label = ttk.Label(self.mainframe, text="x-coordinate:")
        self.pointB_y_label = ttk.Label(self.mainframe, text="y-coordinate:")
        self.pointB_x_input = ttk.Entry(self.mainframe)
        self.pointB_y_input = ttk.Entry(self.mainframe)    
        # self.enter_button: Enter button at the bottom of the window
        self.enter_button = ttk.Button(self.mainframe, text="Enter", command=controller.enter_button_click)

        # Place widgets inside frame
        self.problem_description.grid(column=0, row=0, columnspan=6)
        self.user_instructions.grid(column=0, row=1, pady=(20,20), columnspan=6)
        self.pointA_label.grid(column=0, row=3, columnspan=6)
        self.pointA_x_label.grid(column=0, row=4, sticky=E)
        self.pointA_x_input.grid(column=1, row=4)
        self.pointA_y_label.grid(column=0, row=5, sticky=E)
        self.pointA_y_input.grid(column=1, row=5)
        self.pointB_label.grid(column=0, row=6, pady=(20,0), columnspan=6)
        self.pointB_x_label.grid(column=0, row=7, sticky=E)
        self.pointB_x_input.grid(column=1, row=7)    
        self.pointB_y_label.grid(column=0, row=8, sticky=E)
        self.pointB_y_input.grid(column=1, row=8)
        self.enter_button.grid(column=0, row=9, pady=(20,0) ,columnspan=6)