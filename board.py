import typing
from typing import *
import car


class Board:
    """
    The Board of the game
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__cars: List[car] = []

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        board = list()
        for row in range(7):
            board.append(list())
            for column in range(7):
                board[row].append('_')
        board[3].append('E')

        for car in self.__cars:
            for cor in car.car_coordinates():
                board[cor[0]][cor[1]] = car.get_name()

        current_stat_str = ''
        for row_i, row in enumerate(board):
            if row_i > 0:
                current_stat_str += '\n'
            for col in row:
                current_stat_str += col
        return current_stat_str

    def cell_list(self) -> List:
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        cell_list = list()
        for row in range(7):
            for column in range(7):
                cell_list.append((row, column))
        cell_list.append(self.target_location())
        return cell_list

    def possible_moves(self) -> List[Tuple]:
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        board_possible_moves = []
        for car in self.__cars:
            car_possible_moves: typing.Dict = car.possible_moves()  # {'d': "cause the...."}
            for possible_move, description in car_possible_moves.items():
                empty_cell_needed: Tuple = car.movement_requirements(possible_move)[
                    0]  # car in locations [(1,2),(2,2)] requires [(3,2)]
                if empty_cell_needed in self.cell_list() and not self.cell_content(empty_cell_needed):
                    board_possible_moves.append((car.get_name(), possible_move, description))
        return board_possible_moves

    def target_location(self) -> Tuple:
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return 3, 7

    def cell_content(self, coordinate: typing.Tuple) -> Optional:
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.__cars:
            if coordinate in car.car_coordinates():
                return car.get_name()
        return

    def add_car(self, car) -> bool:
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        for board_car in self.__cars:
            if car.get_name() == board_car.get_name():
                return False

        for coordinate in car.car_coordinates():
            if self.cell_content(coordinate) or (coordinate not in self.cell_list()):
                return False
        self.__cars.append(car)
        return True

    def move_car(self, name: str, movekey: str):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        # self.possible_moves-[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]

        for car_description in self.possible_moves():
            if name == car_description[0] and movekey == car_description[1]:
                for car in self.__cars:
                    if name == car.get_name():
                        return car.move(movekey)
        return False
