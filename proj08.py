'''Source Code Header'''


from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project

def main():
    board_size = 10
    ship_list = [5]

    player1_name = "Player 1"
    player2_name = "Player 2"

    player1_board = Board(size=board_size)
    player1 = Player(name=player1_name, board=player1_board, ship_list=ship_list)

    player2_board = Board(size=board_size)
    player2 = Player(name=player2_name, board=player2_board, ship_list=ship_list)

    game = BattleshipGame(player1=player1, player2=player2)

    game.play()


if __name__ == "__main__":
    main()