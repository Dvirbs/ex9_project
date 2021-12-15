from typing import *


class Car:
    """
    Add class description here
    """

    def __init__(self, name: str, length: int, location: tuple, orientation: int):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # check conditions if the inputs is correct
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self) -> List[Tuple]:
        """
        :return: A list of coordinates the car is in
        """
        car_coordinates_list = list()
        row, col = self.__location  # location: A tuple representing the car's head (row, col) location
        if self.__orientation == 1:  # HORIZONTAL
            car_coordinates_list = [(row, col + i) for i in range(self.__length)]
        else:  # VERTICAL
            car_coordinates_list = [(row + i, col) for i in range(self.__length)]
        return car_coordinates_list

    def possible_moves(self) -> Dict:
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        possible_moves_dict = dict()
        if self.__orientation == 1:  # HORIZONTAL
            possible_moves_dict['r'] = 'cause you can move right'
            possible_moves_dict['l'] = 'cause you can move left'
        else:  # VERTICAL
            possible_moves_dict['u'] = 'cause you can move up'
            possible_moves_dict['d'] = 'cause you can move down'
        return possible_moves_dict

    def movement_requirements(self, movekey: str) -> List:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        row, col = self.__location  # location: A tuple representing the car's head (row, col) location
        legal_cell = list()
        if movekey in self.possible_moves().keys():
            if movekey == 'u':
                legal_cell.append((row - 1, col))
            elif movekey == 'd':
                legal_cell.append((row + self.__length, col))
            elif movekey == 'l':
                legal_cell.append((row, col - 1))
            elif movekey == 'r':
                legal_cell.append((row, col + self.__length))

        return legal_cell

    def move(self, movekey) -> bool:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        row, col = self.__location  # location: A tuple representing the car's head (row, col) location
        if movekey in self.possible_moves().keys():
            if movekey == 'u':
                self.__location = (row - 1, col)
            elif movekey == 'd':
                self.__location = (row + 1, col)
            elif movekey == 'l':
                self.__location = (row, col - 1)
            elif movekey == 'r':
                self.__location = (row, col + 1)
            return True
        else:
            return False

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.__name



