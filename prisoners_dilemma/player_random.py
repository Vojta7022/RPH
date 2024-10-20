import random

class MyPlayer:
    '''Player plays Tit-For-Tat strategy'''

    def __init__(self, payoff_matrix, number_of_iterations = None): 
        # Initialize the player with a payoff matrix and number of iterations, which is optional
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.my_moves = []  # List to store the player's moves
        self.other_moves = []  # List to store the opponent's moves

    def select_move(self):
        return random.randint(0,1)

    def record_last_moves(self, my_last_move, other_last_move):
        # Record the last moves of the player and the opponent
        self.my_moves.append(my_last_move)
        self.other_moves.append(other_last_move)