stable_bonus = 25
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for r, c in corners:
            if board[r][c] == self.my_color:
                my_score += stable_bonus
            elif board[r][c] == self.opponent_color:
                opponent_score += stable_bonus