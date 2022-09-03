#this controller responsible for taking user input to model

from tkinter import *
from tkinter import ttk
from view import *
from model import *


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def enter_button_click(self):
        # Get user values
        self.model.pointA_x_coor = self.view.pointA_x_input.get()
        self.model.pointA_y_coor = self.view.pointA_y_input.get()
        self.model.pointB_x_coor = self.view.pointB_x_input.get()
        self.model.pointB_y_coor = self.view.pointB_y_input.get()

        # Validate user input (all values must be integers)
        self.model.valid_input(self.view)