# Figure out which board will win last
# Once it wins, get the final score

import sys
from bingo import *

draw_numbers, board_list = get_game()

for number in draw_numbers:
    for board in board_list:
        update_board(board, number)

    for board in board_list:
        if check_win(board):
            if len(board_list) > 1:
                board_list.remove(board)
            else:
                print(final_score(board, number))  # Answer: 3178
                sys.exit(0)
