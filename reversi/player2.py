import time

class MyPlayer:
    '''Player using Minimax with alpha-beta pruning and depth-limited search'''
    
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)] # All possible directions
    STABLE_BONUS = 25 # Bonus for occupying a corner
    MOBILITY_WEIGHT = 5 # Weight for computing mobility score, which awards more legal moves  
    
    # Initialize the player with the color of the player and the opponent
    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.stones_placed = 4
        self.weight_matrix = [
            [120, -20, 10,  5,  5, 10, -20, 120],
            [-20, -40, -2, -2, -2, -2, -40, -20],
            [10,   -2, 10,  1,  1, 10,  -2,  10],
            [5,    -2,  1,  0,  0,  1,  -2,   5],
            [5,    -2,  1,  0,  0,  1,  -2,   5],
            [10,   -2, 10,  1,  1, 10,  -2,  10],
            [-20, -40, -2, -2, -2, -2, -40, -20],
            [120, -20, 10,  5,  5, 10, -20, 120]
        ]
        self.time_limit = 0.95  # Max 950 ms for decision-making, to be safe and have extra time for calculations
 
    # Select the player's next move based on the current board state
    def select_move(self, board):
        start_time = time.time()
        best_move = None
        depth = 1
        
        while True:
            try:
                move = self.minimax(board, depth, True, float('-inf'), float('inf'), start_time)
                if move:
                    best_move = move[1]
                depth += 1
            except TimeoutError: # Timeout if the time limit is exceeded
                break
        
        self.stones_placed += 1
        return best_move
    
    # Minimax algorithm with alpha-beta pruning and depth-limited search
    # Inspired by this video: https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    def minimax(self, board, depth, is_maximizing, alpha, beta, start_time):
        if time.time() - start_time > self.time_limit:
            raise TimeoutError # Raise an exception if the time limit is exceeded
        
        legal_moves = self.get_legal_moves(board, self.my_color if is_maximizing else self.opponent_color)
        if depth == 0 or not legal_moves:
            return self.evaluate_board(board), None
        
        best_move = None
        if is_maximizing:
            max_eval = float('-inf')
            for move in legal_moves:
                new_board = self.simulate_move(board, move, self.my_color)
                eval_score = self.minimax(new_board, depth - 1, False, alpha, beta, start_time)[0]
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
                
            return max_eval, best_move
        
        else:
            min_eval = float('inf')
            for move in legal_moves:
                new_board = self.simulate_move(board, move, self.opponent_color)
                eval_score = self.minimax(new_board, depth - 1, True, alpha, beta, start_time)[0]
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
                
            return min_eval, best_move
    
    # Get all legal moves for the current player
    def get_legal_moves(self, board, color):
        legal_moves = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                flipped_stones = self.get_flipped_stones(r, c, board, color)
                if flipped_stones > 0:
                    move_score = self.weight_matrix[r][c] + flipped_stones
                    legal_moves.append(((r, c), move_score))
        legal_moves.sort(key=lambda x: x[1], reverse=True) # Sort by move_score (legal_moves[1]) from highest to lowest to help alpha-beta pruning
        
        return [move[0] for move in legal_moves]
    
    # Simulate a move on the board
    def simulate_move(self, board, move, color):
        r, c = move
        new_board = [row[:] for row in board]
        new_board[r][c] = color
        for direction in MyPlayer.DIRECTIONS:
            flipped_stones = self.get_flipped_positions(r, c, board, color, direction)
            for flipped_r, flipped_c in flipped_stones:
                new_board[flipped_r][flipped_c] = color
                
        return new_board
    
    # Get the number of stones that will be flipped by placing a stone at (r, c)
    def get_flipped_stones(self, r, c, board, color):
        if board[r][c] != -1:
            return 0
        return sum(len(self.get_flipped_positions(r, c, board, color, d)) for d in MyPlayer.DIRECTIONS)
    
    # Check if stone is in the board and has the same color
    def check_boundaries(self, r, c, board, color):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == color

    # Get the positions of stones that will be flipped by placing a stone at (r, c) in a certain direction
    def get_flipped_positions(self, r, c, board, color, direction):
        flipped = []
        dr, dc = direction
        r += dr
        c += dc
        while self.check_boundaries(r, c, board, 1 - color):
            flipped.append((r, c))
            r += dr
            c += dc
        if self.check_boundaries(r, c, board, color):
            return flipped
        
        return []
    
    # Evaluate the board based on the player's color    
    def evaluate_board(self, board):
        my_score = 0
        opponent_score = 0
        
        # Count the number of legal moves for each player
        my_mobility = len(self.get_legal_moves(board, self.my_color))
        opponent_mobility = len(self.get_legal_moves(board, self.opponent_color))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == self.my_color:
                    my_score += self.weight_matrix[r][c]
                elif board[r][c] == self.opponent_color:
                    opponent_score += self.weight_matrix[r][c]
        
        # Add extra bonus for occupying corners            
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for r, c in corners:
            if board[r][c] == self.my_color:
                my_score += MyPlayer.STABLE_BONUS
            elif board[r][c] == self.opponent_color:
                opponent_score += MyPlayer.STABLE_BONUS
        
        # Calculate the mobility score based on the difference in legal moves
        # Having more legal moves is beneficial for the player, allowing more flexibility     
        mobility_score = MyPlayer.MOBILITY_WEIGHT * (my_mobility - opponent_mobility)
                    
        return my_score - opponent_score + mobility_score
