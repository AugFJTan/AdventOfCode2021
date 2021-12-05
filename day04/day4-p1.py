# Find the sum of all unmarked numbers on that board
# Then, multiply sum by the number that was just called to get the final score
# Figure out which board will win first

import sys
from bingo import *

draw_numbers, board_list = get_game()

for number in draw_numbers:
    for board in board_list:
        update_board(board, number)
    
    for board in board_list:
        if check_win(board):  
            print(final_score(board, number))  # Answer: 41503
            sys.exit(0)
