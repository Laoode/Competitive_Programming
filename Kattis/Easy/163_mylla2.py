board = [input().strip() for _ in range(3)]  

def check_win(board):
    for row in board:
        if row == "OOO":
            return True
    
    for col in range(3):
        if board[0][col]=='O' and board[1][col]=='O' and board[2][col]=='O':
            return True
    if board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O':
        return True
    if board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O':
        return True
    return False
    
if check_win(board):
    print("Jebb")
else:
    print("Neibb")
