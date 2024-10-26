class MyPlayer:
    '''Player plays greedy by selecting the move that flips the most stones'''
    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
 
    def select_move(self, board):
        legal_moves = [[0 for _ in range(len(board))] for _ in range(len(board))]
        
        for i in range(len(legal_moves)):
            for j in range(len(legal_moves[0])):
                legal_moves[i][j] = self.get_flipped_stones(i, j, board)
                
        return self.get_max_flipped(legal_moves)
    
    def get_flipped_stones(self, r, c, board):
        if board[r][c] != -1:
            return 0
        
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
        return sum(self.get_line_size_any_direction(r, c, board, d) for d in directions)
    
    def get_line_size_any_direction(self, r, c, board, direction):
        count = 0
        dr, dc = direction
        
        i = r + dr
        j = c + dc
        while 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != -1 and board[i][j] == self.opponent_color:
            count += 1
            i += dr
            j += dc
                
        return 0 if (not 0 <= i < len(board)) or (not 0 <= j < len(board[0])) or (board[i][j] == -1) else count
    
    def get_max_flipped(self, array):
        max_value = max([max(row) for row in array])
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == max_value:
                    return (i, j)
    

if __name__ == "__main__":
    def generate_reversi_board():
        # Initialize an 8x8 board with -1 (empty)
        board = [[-1 for _ in range(8)] for _ in range(8)]
        
        # Set the initial positions for a standard Reversi game
        board[3][3] = 1  # My color
        board[3][4] = 0  # Opponent's color
        board[4][3] = 0  # Opponent's color
        board[4][4] = 1  # My color
        
        return board

    board = generate_reversi_board()
    
    p1 = MyPlayer(1, 0)
    print(p1.select_move(board))