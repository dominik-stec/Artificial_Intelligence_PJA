"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl

To run game type in console:
 >> python start_game.py
as Python interpreter command
"""
import random, os


class Traveller:
    """
    class generate map and setup players position with service operating players moves

    Args:
        map_width (int): The map_width is used to generate map with given width value, as default is equal 20,
        map_height (int): The map_height is used to generate map with given height value, as default is equal 10,
        modulo_gates (int): The modulo_gates is used to generate configuration of game over walls and win gates
                            at the end of map, on the right side, as default is equal 3,
        entropy_gates (list): The entropy_gates is two field list value and is used to compare with 'modulo_gates (int)',
                                as result we can setup how strong and what form should have dispersion generated
                                game over walls and win gates, as default is equal [0, 1],

    Attributes:
        map_width (int): This is where we store map_width,
        map_height (int): This is where we store map_height,
        map_matrix (list): This is where we store map view mapping,
        gates_modulo_trimmer (int): This is where we store modulo_gates,
        gates_modulo_entropy (int): This is where we store entropy_gates,
        player_position (list): This is where we store actual player position on map,
        gates_map (list): This is where we store view and position game over walls and win gates,
    """
    def __init__(self, map_width=20, map_height=10, modulo_gates=3, entropy_gates=[0,1]):
        self.map_width = map_width
        self.map_height = map_height
        self.map_matrix = []
        self.gates_modulo_trimmer = modulo_gates
        self.gates_modulo_entropy = entropy_gates
        self.player_position = []
        self.gates_map = []

    def generate_clear_map_matrix(self):
        """This method as first generates how map should look like in first round as mapping matrix of map fields
        """
        for h in range(0, self.map_height + 2):
            part_h = []
            for w in range(0, self.map_width + 3):
                part_h.append(' ')
            self.map_matrix.append(part_h)

    def generate_map_walls(self):
        """This method generates configuration of game over walls and win gates on the maximum right site on the map
            with given configuration value in map_width, map_height, gates_modulo_trimmer, gates_modulo_entropy
        """
        for i in range(0, self.map_width + 3):
            self.map_matrix[0][i] = '#'
            self.map_matrix[self.map_height + 1][i] = '#'
        for i in range(0, self.map_height + 2):
            self.map_matrix[i][0] = '#'
            if i % self.gates_modulo_trimmer == self.gates_modulo_entropy[0] \
            or i % self.gates_modulo_trimmer == self.gates_modulo_entropy[1]:
                self.map_matrix[i][self.map_width + 1] = '#'
                self.map_matrix[i][self.map_width + 2] = '#'

    def generate_start_player_position(self):
        """This method generates random start player position in maximum left site column on the map
        """
        rand = random.randrange(1, self.map_height)
        self.player_position = [1, rand]
        player_pos_x = self.player_position[0]
        player_pos_y = self.player_position[1]
        self.map_matrix[player_pos_y][player_pos_x] = '*'

    def generate_gates_mapping(self):
        """This method generates mapping of exist game over walls and win gates from the game map
        """
        x_coord = self.map_width + 1
        y_coord = []
        for height in range(1, self.map_height + 1):
            if self.map_matrix[height][x_coord] == '#':
                y_coord.append('#')
            elif self.map_matrix[height][x_coord] == ' ':
                y_coord.append(' ')
        self.gates_map = y_coord

    def game_init(self):
        """This method initialize class attributes for first, start run the game, use: generate_clear_map_matrix(),
            generate_map_walls(), generate_start_player_position(), generate_gates_mapping() method
        """
        self.generate_clear_map_matrix()
        self.generate_map_walls()
        self.generate_start_player_position()
        self.generate_gates_mapping()

    def make_move(self, direction):
        """This method listen moves directions of players to change his position with mark move on the map

        Args:
            direction (str): The move player direction
        """
        player_pos_x = self.player_position[0]
        player_pos_y = self.player_position[1]
        # print dash if move is into wall
        move_icon = '-'

        # up
        if direction == 'w':
            # if move up is not in wall
            if not self.map_matrix[player_pos_y - 1][player_pos_x] == '#':
                player_pos_y -= 1
                move_icon = '/'
        # down
        elif direction == 's':
            # if move down is not in wall
            if not self.map_matrix[player_pos_y + 1][player_pos_x] == '#':
                player_pos_y += 1
                move_icon = '\\'
        # move on right
        player_pos_x += 1
        # mark move on map
        self.map_matrix[player_pos_y][player_pos_x] = move_icon
        # actualize player position
        self.player_position = [player_pos_x, player_pos_y]

    def print_map(self):
        """The method print actual map view on the console
        """
        # clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        # print actual map matrix
        for height in self.map_matrix:
            for width in height:
                print(width, end='')
            print()

    def is_game_over(self):
        """The method check if last player move was done

        Returns:
            bool: A flag with game over state
        """
        if self.player_position[0] == self.map_width + 1:
            return True

    def negamax_win_condition(self, position_before_move):
        """The method check condition for next player move prepared for 'Negamax' artificial intelligence algorithm

            Args:
                position_before_move (list): This field is actual player position, before making move
                                                calculated by 'Negamax' AI algorithm

            Returns:
                bool: A flag inform if actual move should be into game over wall or win gate
        """
        coord_y_prev = position_before_move[1]
        actual_position = self.get_position().copy()
        coord_y_actual = actual_position[1]
        gates = self.get_gates_map()
        gates_map_size = len(gates)
        print(coord_y_prev, coord_y_actual)

        # for move up / coord_y -= 1
        if coord_y_prev > coord_y_actual:
            # iteration size of mapped gates list
            for gate in range(1, gates_map_size+1):
                # if player is in the same line with gate / the same coord y
                if coord_y_actual == gate:
                    # if gate on up direction is wall
                    if gates[gate-1] == '#':
                        # hit in wall, not free gate
                        return True

        # for move down / coord_y += 1
        if coord_y_prev < coord_y_actual:
            for gate in range(1, gates_map_size+1):
                if coord_y_actual == gate:
                    # if gate on down direction is wall
                    if gates[gate-1] == '#':
                        return True

        # for max up position
        if coord_y_prev == coord_y_actual:
            if coord_y_actual == 1:
                return True

        # for max down position
        if coord_y_prev == coord_y_actual:
            if coord_y_actual == self.map_height - 1:
                return True

        return False

    def get_position(self):
        """The method is getter for actual player position on the map

        Returns:
            list: A actual player position
        """
        return self.player_position

    def get_gates_map(self):
        """The method is getter for actual map of game over walls and win gates

        Returns:
            list: A actual map of game over walls and win gates
        """
        return self.gates_map
