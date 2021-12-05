def get_game():
    with open('input.txt', 'r') as file:
        draw_numbers = file.readline().rstrip().split(',')
        board_list = []
        
        while file.readline():
            board = []
            
            for _ in range(5):
                board_row = file.readline().rstrip().split()
                board_result = [[col, False] for col in board_row]
                board.append(board_result)
            
            board_list.append(board)
    
    return draw_numbers, board_list


def update_board(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j][0] == number:
                board[i][j][1] = True
                return


def check_win(board):
    for i in range(5):
        row_bingo = True
        col_bingo = True
    
        for j in range(5):
            if board[i][j][1] == False:
                row_bingo = False
            if board[j][i][1] == False:
                col_bingo = False
        
        if row_bingo or col_bingo:
            return True

    return False


def final_score(board, number):
    score = 0
    
    for j in range(5):
        for i in range(5):
            if board[i][j][1] == False:
                score += int(board[i][j][0])
    
    return score * int(number)
