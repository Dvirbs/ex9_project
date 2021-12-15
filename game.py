import helper
import car
import board


class Game:
    VERTICAL = 0

    """
    game of rush hour
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board

    def __legal_car_name(self, name: str):
        """
        check if car name is legal
        :return: True if name is legal
        """
        if (len(name) != 1) or (type(name) != str) or name.islower():
            return False
        return True

    def __legel_car_move(self, name: str, direction: str):
        """
        check the the move is legal
        :param direction: the direction of the move
        :return: True it is legal
        """
        if direction != ('u' or 'd' or 'l' or 'r'):
            return False
        for possible_move in self.__board.possible_moves():  # [('O','d',"some description"),('R','r',"some description")]
            possible_name = possible_move[0]
            possible_direction = possible_move[1]
            if name == possible_name and direction == possible_direction:
                return True

        return False

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        print(self.__board)
        inp = str(input('\n*** write the car color and direction that you wont to move : *** '))
        if len(inp)<3:
            inp = str(input('\n*** input not correct!(for Yellow car move down type --> Y,d) *** '))
        car_name = inp[0]
        move_direction = inp[2]
        while not (self.__legal_car_name(car_name) or self.__legel_car_move(car_name, move_direction)):
            inp = str(input('\n*** input not correct!(for Yellow car move down type --> Y,d) *** '))
            car_name = inp[0]
            move_direction = inp[2]
        self.__board.move_car(car_name, move_direction)
        print('\n', self.__board)

    def __not_game_ended(self):
        """
        check if the game not ended
        :return: True if the game not ended
        """
        target_location = self.__board.target_location()
        if target_location != '!':
            return True
        target_content = self.__board.cell_content(target_location)
        if target_content is not None:
            car_name = target_content
            info = helper.load_json('car_config.json')[car_name]
            orientation = info[2]
            if orientation == self.VERTICAL:
                return True
        return False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while self.__not_game_ended():
            self.__single_turn()


def not_legal_car(name: str, length: int, orientation: int):
    """
    check if car is legal
    :return: True if car not legal
    """
    if (len(name) != 1) or (type(name) != str) or name.islower():
        return True
    elif (not 2 <= length <= 4) or (orientation != (1 or 0)):
        return True
    else:
        return False


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    game_board = board.Board()
    for name, info in helper.load_json('car_config.json').items():
        length = info[0]
        location = tuple(info[1])
        orientation = info[2]
        if not_legal_car(name, length, orientation):
            continue
        elif location not in game_board.cell_list():
            continue

        the_car = car.Car(name, length, location, orientation)
        game_board.add_car(the_car)
    game = Game(game_board)
    game.play()

