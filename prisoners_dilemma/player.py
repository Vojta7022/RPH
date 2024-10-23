import random

class MyPlayer:
    '''Tit-For-Tat strategy by default, adjusts based on various parameters'''
    
    COOPERATE = False
    DEFECT = True 
    
    # Threshold for determining strategy based on payoff differences
    PAYOFF_THRESHOLD = 20

    # Initialize the player with a payoff matrix and an optional number of iterations.
    # The matrix is analyzed to determine the default strategy.
    def __init__(self, payoff_matrix, number_of_iterations=None):
        
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.my_moves = []            # Stores the player's moves throughout the game
        self.other_moves = []         # Stores the opponent's moves
        self.selected_move = None     # Move selected in select_move, used for detecting noise
        self.strategy = "tit-for-tat" # Default strategy is Tit-For-Tat
        self.analyze_matrix()         # Analyze the payoff matrix at initialization

    # Select the player's next move based on the current strategy.
    def select_move(self):
        
        # Defect in the final round
        if self.number_of_iterations and len(self.my_moves) == self.number_of_iterations - 1:
            self.selected_move = MyPlayer.DEFECT
        
        elif self.strategy == "always_defect":
            self.selected_move = MyPlayer.DEFECT
        
        elif self.strategy == "always_cooperate":
            self.selected_move = MyPlayer.COOPERATE
        
        # Occasionally defect if the opponent defects more than 30% of the time (random element for unpredictability)
        elif (len(self.other_moves) > 5 and sum(self.other_moves) / len(self.other_moves) > 0.3) and random.random() < 0.05:
            return MyPlayer.DEFECT
        
        # Tit-for-Two-Tats strategy: Defect only after two consecutive opponent defections
        elif self.strategy == "tit_for_two_tats":  # Played when noise detected
            if (self.other_moves[-1] == MyPlayer.DEFECT and self.other_moves[-2] == MyPlayer.DEFECT):
                self.selected_move = MyPlayer.DEFECT
            else:
                self.selected_move = MyPlayer.COOPERATE
        
        # Default Tit-For-Tat strategy: Mirror the opponent's last move
        else:
            self.selected_move = self.other_moves[-1] if len(self.other_moves) > 0 else MyPlayer.COOPERATE
        
        return self.selected_move

    # Record the last moves made by the player and the opponent..
    def record_last_moves(self, my_last_move, other_last_move):
        
        self.my_moves.append(my_last_move)
        self.other_moves.append(other_last_move)
        
        # Detect noise (when selected move does not match the actual recorded move) and switch to more forgiving strategy
        if self.selected_move != self.my_moves[-1]:
            self.strategy = "tit_for_two_tats"  # Noise detected, switch to a more forgiving strategy

    def analyze_matrix(self):
        # Analyze the payoff matrix to determine the optimal default strategy based on the rewards and punishments.
        mutual_coop = self.payoff_matrix[0][0][0]      # Payoff when both cooperate
        coop_vs_defect = self.payoff_matrix[0][1][0]   # Payoff when I cooperate, opponent defects
        defect_vs_coop = self.payoff_matrix[1][0][0]   # Payoff when I defect, opponent cooperates
        mutual_defect = self.payoff_matrix[1][1][0]    # Payoff when both defect
        
        # Strategy determination based on relative differences in payoffs
        # if defect_vs_coop - coop_vs_defect > MyPlayer.PAYOFF_THRESHOLD:
        #     self.strategy = "always_defect"
        # elif coop_vs_defect - defect_vs_coop > MyPlayer.PAYOFF_THRESHOLD:
        #     self.strategy = "always_cooperate"
        if mutual_coop > mutual_defect and defect_vs_coop > coop_vs_defect:
            self.strategy = "tit_for_tat"
        elif defect_vs_coop > mutual_coop and mutual_defect > coop_vs_defect:
            self.strategy = "always_defect"
        elif mutual_coop > defect_vs_coop and coop_vs_defect > mutual_defect:
            self.strategy = "always_cooperate"
