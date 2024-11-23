import time

class MyPlayer:
    '''Player using Minimax with alpha-beta pruning and depth-limited search'''
    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
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
        self.time_limit = 0.95  # Max 950 ms for decision-making

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
            except TimeoutError:
                break

        return best_move

    def minimax(self, board, depth, is_maximizing, alpha, beta, start_time):
        if time.time() - start_time > self.time_limit:
            raise TimeoutError
        
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

    def get_legal_moves(self, board, color):
        legal_moves = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                flipped_stones = self.get_flipped_stones(r, c, board, color)
                if flipped_stones > 0:
                    move_score = self.weight_matrix[r][c] + flipped_stones
                    legal_moves.append(((r, c), move_score))
        legal_moves.sort(key=lambda x: x[1], reverse=True)
        return [move[0] for move in legal_moves]


    def simulate_move(self, board, move, color):
        r, c = move
        new_board = [row[:] for row in board]
        new_board[r][c] = color
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
        for dr, dc in directions:
            flipped = self.get_flipped_positions(r, c, board, color, (dr, dc))
            for fr, fc in flipped:
                new_board[fr][fc] = color
        return new_board

    def get_flipped_stones(self, r, c, board, color):
        if board[r][c] != -1:
            return 0
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
        return sum(len(self.get_flipped_positions(r, c, board, color, d)) for d in directions)

    def get_flipped_positions(self, r, c, board, color, direction):
        flipped = []
        dr, dc = direction
        i, j = r + dr, c + dc
        while 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == (1 - color):
            flipped.append((i, j))
            i += dr
            j += dc
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == color:
            return flipped
        return []

    def evaluate_board(self, board):
        my_score = 0
        opponent_score = 0
        my_mobility = len(self.get_legal_moves(board, self.my_color))
        opponent_mobility = len(self.get_legal_moves(board, self.opponent_color))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == self.my_color:
                    my_score += self.weight_matrix[r][c]
                elif board[r][c] == self.opponent_color:
                    opponent_score += self.weight_matrix[r][c]

        stable_bonus = 25
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for r, c in corners:
            if board[r][c] == self.my_color:
                my_score += stable_bonus
            elif board[r][c] == self.opponent_color:
                opponent_score += stable_bonus

        mobility_weight = 5
        mobility_score = mobility_weight * (my_mobility - opponent_mobility)

        return my_score - opponent_score + mobility_score

if __name__ == "__main__":
    def generate_reversi_board():
        board = [[-1 for _ in range(8)] for _ in range(8)]
        board[3][3] = 1
        board[3][4] = 0
        board[4][3] = 0
        board[4][4] = 1
        return board

    board = generate_reversi_board()
    player = MyPlayer(1, 0)
    print(player.select_move(board))
