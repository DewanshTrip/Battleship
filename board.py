class Ship(object):
    """
        add your Class header here.
    """
    def __init__(self, length, position, orientation):
        """
            Intialize ship attributes and variables
        """
        self.length = length
        self.position = position
        self.orientation = orientation
        self.hit_count = 0
        self.is_sunk = False


        row, col = self.position
        self.position = []

        if self.orientation == 'h':
            self.position = [(row, col + i) for i in range(self.length)]
        elif self.orientation == 'v':
            self.position = [(row + i, col) for i in range(self.length)]


    def get_positions(self):
        """
            Gets ship position
        """
        return self.position

    def get_orientation(self):
        """
            Gets ship orientation
        """
        return self.orientation

    def apply_hit(self):
        """
            Applies hit to ship and checks if ship is sunk
        """
        self.hit_count += 1
        if self.hit_count == self.length:
            self.is_sunk = True



class Board(object):
    """
        add your Class header here.
    """
    def __init__(self, size):
        """
            Intializes attributes and variables for class Board
        """
        self.size = size
        self.board = [[' ' for x in range(size)] for y in range(size)]
        self.ships = []

    def place_ship(self, ship):
        """
        Places ship on board
        """
        self.ships.append(ship)
        positions = ship.get_positions()

        for position in positions:
            row, col = position
            self.board[row][col] = "S"
            

    def apply_guess(self, guess):
        """
        Takes guess and checks to see if guess hit any ships
        """
        row, col = guess
        hit_ship = None
        for ship in self.ships:
            positions = ship.get_positions()    
            if (row, col) in positions:
                hit_ship = ship
                break
        
        if hit_ship:
            hit_ship.apply_hit()
            self.board[row][col] = "H"
            print("Hit!")
        else:
            self.board[row][col] = "M"
            print("Miss!")

    def validate_ship_coordinates(self, ship):
        """
            Checks to see if ship position is in the board and not already taken
        """
        for position in ship.get_positions():
            row, col = position

            if not (0 <= row < self.size) or not (0 <= col < self.size):
                raise RuntimeError("Ship coordinates are out of bounds!")
            
            if self.board[row][col] == "S":
                raise RuntimeError("Ship coordinates are already taken!")


    def __str__(self):
        """
            Returns fully displayed board
        """
        board_str = ""
        for row in self.board:
            row_str = "[" + "][".join(row) + "]\n"
            board_str += row_str
    
        return board_str
