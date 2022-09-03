# method calucaltes the manhattan distance between two points
# It is calculated by only taking the vertical and horiazantal paths.
# It will takes Tuple as input and returen integer. Return value is between those points

from unittest import result


def manhattan_distance(first_point, second_point):
    #calculate the horizantal distance: |x1-x2|
    x_distance = abs(first_point[0] - second_point[0])

    #calculate the horizantal distance: |y1-y2|
    y_distance = abs(first_point[1] - second_point[1])

    #total distance
    total_distance = x_distance + y_distance

    return total_distance


# This method validates user input to ensure the user is entering integer values for the co-ordinates
# This method takes in input and cast it to an integer. If cast is successfully, this method return true otherwise false.

def valid_input(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


#this main method will continue to ask user for input untill the calculation finish

if __name__ == "__main__":
    print("Enter the point A and point B to calculate the manhattan distance.")

    #Vaildate Input
    while True:
        #prompt user to enter the x-coordinate for the first point
        first_x_cod =  input("Enter the x-coordinate of the first point")
        while not valid_input(first_x_cod):
            print("OOPS!, Input seems wrong")
            first_x_cod =  input("Enter the x-coordinate of the first point")

        #prompt user to enter the y-coordinate for the first point
        first_y_cod =  input("Enter the y-coordinate of the first point")
        while not valid_input(first_y_cod):
            print("OOPS!, Input seems wrong")
            first_y_cod =  input("Enter the y-coordinate of the first point")

        #prompt user to enter the x-coordinate for the second point
        second_x_cod =  input("Enter the x-coordinate of the second point")
        while not valid_input(second_x_cod):
            print("OOPS!, Input seems wrong")
            second_x_cod =  input("Enter the x-coordinate of the second point")

        #prompt user to enter the y-coordinate for the second point
        second_y_cod =  input("Enter the y-coordinate of the second point")
        while not valid_input(second_y_cod):
            print("OOPS!, Input seems wrong")
            second_y_cod =  input("Enter the y-coordinate of the second point")


        #create points
        first_point = (int(first_x_cod), int(first_y_cod))
        second_point = (int(second_x_cod), int(second_y_cod))


        #calculate the manhantta distance and print the values
        result = manhattan_distance(first_point, second_point)
        print("The Manhattan distance is : " + str(result))

        # Escape root
        user_input = input("Would you like calcuate next co-ordinate? (y/n):")
        if user_input == 'n':
            break

