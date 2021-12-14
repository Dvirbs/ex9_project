import typing
import car
import json
import helper
from typing import *


class Board:
    """
    The Board of the game
    """
    DEST = (3, 7)

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__cars: typing.Dict = helper.load_json('car_config.json')  # List of car the add after checking the conditions for add car in the methead add_car
                                    # TODO- need to check if the car name is correct and lengh and everyting
        self.__board_list: typing.List = self.__board_initial()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        current_stat_str = ''
        board = self.__board_list
        for row_i, row in enumerate(board):
            if row_i > 0:
                current_stat_str += '\n'
            for col in row:
                #TODO need to change when i will know what object will be in the board
                current_stat_str += str(col)
        return current_stat_str

    def __board_initial(self):
        """
        initial the board
        :return: 2D lists with exit in (3,7)
        """
        board = list()
        for row in range(7):
            board.append(list())
            for column in range(7):
                board[row].append((row, column))
        board[3].append(self.DEST)
        return board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        # for row_i, row in enumerate(self.board_initial):
        return self.__board_list

    def all_cars_coordinate(self) -> typing.List[typing.Tuple]:
        """
        getting all coordinates of the cars in board
        :return: list of tuple
        """
        cars = self.__cars
        all_cars_cord = list()
        for car in cars:
            all_cars_cord += car.car_coordinates()
        return all_cars_cord



    def possible_moves(self) -> List[Tuple]:
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        cars = self.__cars
        board_possible_moves = list()
        cars_positions = self.all_cars_coordinate()
                        # TODO - need to check what is the object car in the sef.__cars
        if len(cars) == 0:
            return board_possible_moves
        else:
            # TODO maybe can write the next loops in smarter way
            for car in cars.keys():
                car_possible_moves: typing.Dict = car.possible_moves()  # {'d': "cause the...."}
                for possible_move in car_possible_moves.keys():
                    empty_cell_needed: List[Tuple] = car.movement_requirements(possible_move)  # car in locations [(1,2),(2,2)] requires [(3,2)]
                    if empty_cell_needed in self.cell_list() and empty_cell_needed not in cars_positions:
                        board_possible_moves.append((car.get_name(), possible_move, 'do what feels you good'))
                    




    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return self.DEST

    def cell_content(self, coordinate: typing.Tuple):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        # ??? to check what happed if the cordinate not in the board ???
        pass

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        pass

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        pass


if __name__ == '__main__':
    my_board = Board()
    print(my_board)