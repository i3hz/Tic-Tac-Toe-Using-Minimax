X = 'X'
O = 'O'
board = [['X', 'O', 'X'],
         ['X', 'O', 'O'],
         ['O', 'O', 'X']]
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if [X,X,X] in board:
        return X
    if {O,O,O} in board:
        return O
    if board[1][1]==board[2][2] and board[1][1]==board[0][0]:
        return board[1][1]
    if board[0][2]==board[1][1] and board[0][2]== board[2][0]:
        return board[0][2]
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i] 
            
    return None

print(winner(board))
