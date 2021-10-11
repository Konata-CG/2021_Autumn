import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


# don't change the class name
class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your
        # decision
        self.candidate_list = []


# The input is current chessboard.
def go(self, chessboard):
    # Clear candidate_list, must do this step
    self.candidate_list.clear()

    # ==================================================================
    # Write your algorithm here
    # Here is the simplest sample:Random decision
    # row : idx[0], column : idx[1]
    idx = np.where(chessboard == COLOR_NONE)
    idx = list(zip(idx[0], idx[1]))

    # ==============Find new pos========================================
    # Make sure that the position of your decision in chess board is empty.
    # If not, the system will return error.
    # Add your decision into candidate_list, Records the chess board
    # You need add all the positions which is valid
    # candidate_list example: [(3,3),(4,4)]
    # You need append your decision at the end of the candidate_list,
    # we will choice the last element of the candidate_list as the position you choose
    # If there is no valid position, you must return an empty list.
    neighbor = {}
    for pos in idx:
        # check have neighbor in opposite color
        if chessboard[pos[0] + 1][pos[1] + 1] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] + 1][pos[1] - 1] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] + 1][pos[1]] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] - 1][pos[1] + 1] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] - 1][pos[1] - 1] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] - 1][pos[1]] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] + 1][pos[1] + 1] == (self.color or COLOR_NONE) and \
                chessboard[pos[0] + 1][pos[1] - 1] == (self.color or COLOR_NONE):
            continue

        # check all positions in the same row / column / diagonal
        # find the nearest position which is in the same color, add it into neighbor list
        neighbor[pos] = []
        # column_down
        if pos[0] < self.chessboard_size - 1:
            for row_idx in [pos[0] + 1, self.chessboard_size - 1]:
                if chessboard[row_idx][pos[1]] == self.color:
                    neighbor[pos].append((row_idx, pos[1]))
                    break
                elif chessboard[row_idx][pos[1]] != COLOR_NONE:
                    continue
                else:
                    break

        # column_up
        if pos[0] > 0:
            for row_idx in [0, pos[0] - 1]:
                if chessboard[(pos[0] - 1) - row_idx][pos[1]] == self.color:
                    neighbor[pos].append(((pos[0] - 1) - row_idx, pos[1]))
                    break
                elif chessboard[(pos[0] - 1) - row_idx][pos[1]] != COLOR_NONE:
                    continue
                else:
                    break
        # row_left
        if pos[1] < self.chessboard_size - 1:
            for col_idx in [pos[1] + 1, self.chessboard_size - 1]:
                if chessboard[pos[0]][col_idx] == self.color:
                    neighbor[pos].append((pos[0])(col_idx))
                    break
                elif chessboard[pos[0]][col_idx] != COLOR_NONE:
                    continue
                else:
                    break
        # row_right
        if pos[1] > 0:
            for col_idx in [0, pos[1] - 1]:
                if chessboard[pos[0]][(pos[1] - 1) - col_idx] == self.color:
                    neighbor[pos].append((pos[0])((pos[1] - 1) - col_idx))
                    break
                elif chessboard[pos[0]][(pos[1] - 1) - col_idx] != COLOR_NONE:
                    continue
                else:
                    break
        # diagonal_right_down
        if pos[1] < self.chessboard_size - 1 and pos[0] < self.chessboard_size - 1:
            row_idx = pos[0] + 1
            col_idx = pos[1] + 1
            while row_idx <= self.chessboard_size - 1 and col_idx <= self.chessboard_size - 1:
                if chessboard[row_idx][col_idx] == self.color:
                    neighbor[pos].append((row_idx, col_idx))
                    break
                elif chessboard[row_idx][col_idx] != COLOR_NONE:
                    row_idx = row_idx + 1
                    col_idx = col_idx + 1
                    continue
                else:
                    break
        # diagonal_right_up
        if pos[1] < self.chessboard_size - 1 and pos[0] > 0:
            row_idx = pos[0] - 1
            col_idx = pos[1] + 1
            while row_idx >= 0 and col_idx <= self.chessboard_size - 1:
                if chessboard[row_idx][col_idx] == self.color:
                    neighbor[pos].append((row_idx, col_idx))
                    break
                elif chessboard[row_idx][col_idx] != COLOR_NONE:
                    row_idx = row_idx - 1
                    col_idx = col_idx + 1
                    continue
                else:
                    break
        # diagonal_left_up
        if pos[1] > 0 and pos[0] > 0:
            row_idx = pos[0] - 1
            col_idx = pos[1] - 1
            while row_idx >= 0 and col_idx >= 0:
                if chessboard[row_idx][col_idx] == self.color:
                    neighbor[pos].append((row_idx, col_idx))
                    break
                elif chessboard[row_idx][col_idx] != COLOR_NONE:
                    row_idx = row_idx - 1
                    col_idx = col_idx - 1
                    continue
                else:
                    break
        # diagonal_left_down
        if pos[1] > 0 and pos[0] < self.chessboard_size - 1:
            row_idx = pos[0] + 1
            col_idx = pos[1] - 1
            while row_idx <= self.chessboard_size - 1 and col_idx >= 0:
                if chessboard[row_idx][col_idx] == self.color:
                    neighbor[pos].append((row_idx, col_idx))
                    break
                elif chessboard[row_idx][col_idx] != COLOR_NONE:
                    row_idx = row_idx + 1
                    col_idx = col_idx - 1
                    continue
                else:
                    break

        # check pos valid
        if len(neighbor[pos]) != 0:
            self.candidate_list.append(pos)
