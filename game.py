from board import Ship,Board 
import sys


def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str

class Player(object):
    """
    Represents a player in the Battleship game.
    """

    def __init__(self, name, board, ship_list):
        """
        Initializes a player with a name, a board, and a list of ship lengths.
        """
        self.name = name
        self.board = board
        self.ship_list = ship_list
        self.ships = []

    def validate_guess(self, guess):
        """
        Validates if the guess is within the board boundaries.
        """
        row, col = guess
        if not (0 <= row < self.board.size) or not (0 <= col < self.board.size):
            raise RuntimeError("Guess is not a valid location!")

    def get_player_guess(self):
        """
        Gets a valid guess from the player.
        """
        while True:
            try:
                guess_str = input("Enter your guess: ")
                row, col = map(int, guess_str.split(','))

                self.validate_guess((row, col))

                return row, col

            except ValueError:
                print("Invalid input format. Please enter in the format 'row,col'.")
            except RuntimeError as e:
                print(f"Error: {e}. Please enter a valid guess.")

    def set_all_ships(self):
        """
        Places all ships on the board based on the ship_list.
        """
        for ship_size in self.ship_list:
            while True:
                try:
                    coordinates_str = input(f"Enter the coordinates of the ship of size {ship_size}: ")
                    row, col = map(int, coordinates_str.split(','))

                    orientation = input(f"Enter the orientation of the ship of size {ship_size}: ")

                    new_ship = Ship(length=ship_size, position=(row, col), orientation=orientation)
                    self.board.validate_ship_coordinates(new_ship)
                    self.board.place_ship(new_ship)
                    self.ships.append(new_ship)
                    break

                except ValueError:
                    print("Invalid input format. Please enter coordinates in the format 'row,col'.")
                except RuntimeError as e:
                    print(f"{e}")



class BattleshipGame(object):
    """
        Intiailizes and codes the game
    """

    def __init__(self, player1, player2):
        """
            Intializes the players
        """
        self.player1 = player1
        self.player2 = player2

    def check_game_over(self):
        """
            Check if the game has ended.
            Returns the winning player or None if the game is not over.
        """
    
        if all(ship.is_sunk for ship in self.player1.ships):
            return self.player2

        if all(ship.is_sunk for ship in self.player2.ships):
            return self.player1

        # Return None if the game is not over
        return None

    def display(self):
        """
            Displaying both players boards
        """
        print("Player 1's board:")
        print(self.player1.board)


        print("Player 2's board:")
        print(self.player2.board)
        

    def play(self):
        """
            The main function for beginning the game
        """
        
        self.player1.set_all_ships()
        self.player2.set_all_ships()

        while True:
            # Part Two: Players start trying to sink each other's ships
            print("Player 1's board:")
            print(self.player1.board)

            print("Player 2's board:")
            print(self.player2.board)

            # Player 1's turn
            print("{}'s turn.".format(self.player1.name))
            guess1 = self.player1.get_player_guess()
            self.player2.board.apply_guess(guess1)
            if self.check_game_over() == self.player1:
                print("{} wins!".format(self.player1.name))
                break

            # Player 2's turn
            print("{}'s turn.".format(self.player2.name))
            guess2 = self.player2.get_player_guess()
            self.player1.board.apply_guess(guess2)
            if self.check_game_over() == self.player2:
                print("{} wins!".format(self.player2.name))
                break

            # Ask players if they want to continue playing
            continue_playing = input("Continue playing?: ")
            if continue_playing.lower() == 'q':
                break
