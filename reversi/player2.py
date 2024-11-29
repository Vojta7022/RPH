class MyPlayer:
    """Hrac kombinuje greedy strategii a umistovani kamenu na vyhodna mista"""

    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color

    def select_move(self, board):
        valid_moves = self.get_valid_moves(board)
        if len(valid_moves) > 0:
            move = self.choose_best_move(valid_moves, board)
            return move
        else:
            return None

    def choose_best_move(self, moves, board):
        best_move = moves[0]
        best_score = 0

        for move in moves:
            score = self.get_move_score(move[0], move[1], board)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def get_move_score(self, r, c, board):
        ranked_board = [
            [120, -20, 10,  5,  5, 10, -20, 120],
            [-20, -40, -2, -2, -2, -2, -40, -20],
            [10,   -2, 10,  1,  1, 10,  -2,  10],
            [5,    -2,  1,  0,  0,  1,  -2,   5],
            [5,    -2,  1,  0,  0,  1,  -2,   5],
            [10,   -2, 10,  1,  1, 10,  -2,  10],
            [-20, -40, -2, -2, -2, -2, -40, -20],
            [120, -20, 10,  5,  5, 10, -20, 120]
        ]

        directions = [
            (1, 1),
            (1, 0),
            (0, 1),
            (-1, -1),
            (-1, 0),
            (0, -1),
            (-1, 1),
            (1, -1),
        ]
        score = 0
        for dir in directions:
            cur_r, cur_c = r + dir[0], c + dir[1]
            temp_score = 0
            while (
                self.is_on_board(cur_r, cur_c, board)
                and board[cur_r][cur_c] == self.opponent_color
            ):
                temp_score += ranked_board[r][c]
                cur_r += dir[0]
                cur_c += dir[1]
            if (
                self.is_on_board(cur_r, cur_c, board)
                and board[cur_r][cur_c] == self.my_color
            ):
                score += temp_score
        return score

    def get_valid_moves(self, board):
        valid_moves = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if self.is_move_valid(r, c, board):
                    valid_moves.append((r, c))
        return valid_moves

    def is_move_valid(self, r, c, board):
        if board[r][c] == -1:
            directions = [
                (1, 1),
                (1, 0),
                (0, 1),
                (-1, -1),
                (-1, 0),
                (0, -1),
                (-1, 1),
                (1, -1),
            ]
            for dir in directions:
                if self.is_dir_valid(r, c, board, dir):
                    return True
        return False

    def is_dir_valid(self, r, c, board, dir):
        cur_r = r + dir[0]
        cur_c = c + dir[1]
        opp_found = False
        while (
            self.is_on_board(cur_r, cur_c, board)
            and board[cur_r][cur_c] == self.opponent_color
        ):
            opp_found = True
            cur_r += dir[0]
            cur_c += dir[1]

        if (
            opp_found
            and self.is_on_board(cur_r, cur_c, board)
            and board[cur_r][cur_c] == self.my_color
        ):
            return True
        else:
            return False

    def is_on_board(self, r, c, board):
        return r >= 0 and c >= 0 and r < len(board) and c < len(board[r])
