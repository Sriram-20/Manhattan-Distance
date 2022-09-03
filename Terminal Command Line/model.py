#This is responsible for hoilding user Input, performing vakidation and calculating the anhattan distance

from view import *

class Model:
    #Intialize the model with necessary variable

    def __init__(self):
        self.pointA_x_coor = None
        self.pointA_y_coor = None
        self.pointB_x_coor = None
        self.pointB_y_coor = None
        self.pointA = None
        self.pointA = None


        # this method calculate the manhattan distance 
        #Manhattan Distance = abs(pointA(x-coordinate) - pointB(x-coordinate)) +  abs(pointA(y-coordinate) - pointB(y-coordinate))
        
    def manhattan_distance(self, view):
        # Calculate the horizontal distance: | x1 - x2 |
        x_distance = abs(self.point_A[0] - self.point_B[0])

        # Calculate the vertical distance: | y1 - y2 |
        y_distance = abs(self.point_A[1] - self.point_B[1])

        # Total distance is horizontal distance + vertical distance
        total_distance = x_distance + y_distance

       
        result = f"The Manhattan distance between {x_distance} and {y_distance} is {total_distance} units"
        tkinter.messagebox.showinfo(title="Result", message=result)

    # This method validates user input. All values enterted must be integers.
    def valid_input(self, view):
        # Try to cast user values to int. If this fails, print an error.
        try:
            self.pointA_x_coor = int(self.pointA_x_coor)
            self.pointA_y_coor = int(self.pointA_y_coor)
            self.pointB_x_coor = int(self.pointB_x_coor)
            self.pointB_y_coor = int(self.pointB_y_coor)

            # Create point A and point B from coordinates
            self.point_A = (self.pointA_x_coor, self.pointA_y_coor)
            self.point_B = (self.pointB_x_coor, self.pointB_y_coor)

            # Calculate Manhattan distance
            self.manhattan_distance(view)
        except:
             tkinter.messagebox.showerror(title="Invalid Input", message="OOPS! Input seems wrong")