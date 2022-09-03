import unittest
import main

class TestMain(unittest.TestCase):

    #point 1: (0,0)
    #point 2: (0,0)
    def test1(self):
        first_point = (0,0)
        second_point = (0,0)
        distance =main.manhattan_distance(first_point,second_point)
        self.assertEqual(distance, 0, "Should be 0")

    # Point 1: (-1,0)
    # Point 2: (0,0)
    # Distance should be 1
    def test2(self):
        first_point = (-1,0)
        second_point = (0,0)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 1, "Should be 1")
    
    # Point 1: (0,0)
    # Point 2: (-1,0)
    # Distance should be 1
    def test3(self):
        first_point = (0,0)
        second_point = (-1,0)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 1, "Should be 1")

    # Point 1: (0,-1)
    # Point 2: (0,0)
    # Distance should be 1
    def test4(self):
        first_point = (0,-1)
        second_point = (0,0)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 1, "Should be 1")

    # Point 1: (0,0)
    # Point 2: (0,-1)
    # Distance should be 1
    def test5(self):
        first_point = (0,0)
        second_point = (0,-1)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 1, "Should be 1")

    # Point 1: (5,4)
    # Point 2: (3,2)
    # Distance should be 4
    def test6(self):
        first_point = (5,4)
        second_point = (3,2)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 4, "Should be 4")

    # Point 1: (-1,2)
    # Point 2: (1,-2)
    # Distance should be 6
    def test7(self):
        first_point = (-1,2)
        second_point = (1,-2)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 6, "Should be 6")

    # Point 1: (-1,1)
    # Point 2: (2,2)
    # Distance should be 4
    def test8(self):
        first_point = (-1,1)
        second_point = (2,2)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 4, "Should be 4")

    # Point 1: (-37,-49)
    # Point 2: (-64,-71)
    # Distance should be 49
    def test9(self):
        first_point = (-37,-49)
        second_point = (-64,-71)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 49, "Should be 49")

    # Point 1: (-10,20)
    # Point 2: (20,10)
    # Distance should be 40
    def test10(self):
        first_point = (-10,20)
        second_point = (20,10)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 40, "Should be 40")

    # Point 1: (-3,-7)
    # Point 2: (1,2)
    # Distance should be 13
    def test11(self):
        first_point = (-3,-7)
        second_point = (1,2)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 13, "Should be 13")

    # Point 1: (-5,-6)
    # Point 2: (-7,8)
    # Distance should be 16
    def test12(self):
        first_point = (-5,-6)
        second_point = (-7,8)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 16, "Should be 16")

    # Point 1: (-1,-2)
    # Point 2: (-3,-4)
    # Distance should be 4
    def test13(self):
        first_point = (-1,-2)
        second_point = (-3,-4)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 4, "Should be 4")

    # Point 1: (324,458)
    # Point 2: (211,104)
    # Distance should be 467
    def test14(self):
        first_point = (324,458)
        second_point = (211,104)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 467, "Should be 467")

    # Point 1: (-123,-456)
    # Point 2: (-789,-987)
    # Distance should be 1197
    def test15(self):
        first_point = (-123,-456)
        second_point = (-789,-987)
        distance = main.manhattan_distance(first_point, second_point)
        self.assertEqual(distance, 1197, "Should be 1197")

if __name__ == '__main__':
    unittest.main()