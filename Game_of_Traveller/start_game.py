"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl

To run game type in console:
 >> python start_game.py
as Python interpreter command

This Python module is PJATK laboratory template modification
"""
from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax
import traveller


class GameOfTravel( TwoPlayersGame ):
    """
    The GameOfTravel instruction:
    In given serial number of moves, the players can choose if go up or down in one move,
     but they always go forward too, the Human_Player try to hit in wall in last move
      and his moves should have this intent, AI_Player try to hit into free gates in his moves
      and avoid to hit in wall, in shortcut Human_Player try to hit in wall,
        the AI_PLayer try to hit in gates, they have the same number of moves in round,
        they have the same figure to move up or down, in game exist only one figure on map to move,
        if AI_Player in his last move hit into wall the Human_Player wins,
        if AI_Player in his last move pass into free gate the Human_Player loses,
     """

    def __init__(self, players):
        self.players = players
        self.nplayer = 1  # player 1 starts
        self.map_width = 20  # map width size
        self.map_height = 10 # map height size
        self.gates_modulo_trimmer = 3  # game over gates count
        self.gates_modulo_entropy = [0, 1] # game over gates dispersion
        self.travel = traveller.Traveller(self.map_width, self.map_height, self.gates_modulo_trimmer, self.gates_modulo_entropy)
        self.travel.game_init()  # initialize map
        self.number_of_moves = 5  # number of moves for player in one round
        self.position_before_move = []

    def possible_moves(self): return ['w', 's']

    def make_move(self, move):
        self.position_before_move = self.travel.get_position()  # remember position before move
        if self.nmove % self.number_of_moves == 0:  # switch player after given number of moves
            self.switch_player()
        self.travel.make_move(move)  # make given number of move
        self.switch_player()  # stay as player for next moves in self round

    def win(self):
        return self.travel.negamax_win_condition(self.position_before_move)  # check next move conditions

    def is_over(self):
        return self.travel.is_game_over()  # game is over if map width is end

    def show(self):
        self.travel.print_map()
        print("type direction:   'w' -> up   |  's' -> down")

    def scoring(self): return 100 if self.win() else 0  # For the AI

ai = Negamax(6)  # The AI will think 6 moves in advance
game = GameOfTravel( [ Human_Player(), AI_Player(ai) ] )
history = game.play()