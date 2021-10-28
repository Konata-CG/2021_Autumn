import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


class Neighbor:
    position = ()
    # distance = 0

    def __init__(self, cur_pos, neighbor_pos):
        self.position = neighbor_pos
        # self.measure_distance(cur_pos)

    # calculate how many rival's chess is between you and your neighbor
    # def measure_distance(self, cur_pos):
    #     if self.position[0] == cur_pos[0]:
    #         if self.position[1] >= cur_pos[1]:
    #             self.distance = self.position[1] - cur_pos[1] - 1
    #         else:
    #             self.distance = cur_pos[1] - self.position[1] - 1
    #     else:
    #         if self.position[0] >= cur_pos[0]:
    #             self.distance = self.position[0] - cur_pos[0] - 1
    #         else:
    #             self.distance = cur_pos[0] - self.position[0] - 1


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

    # give a position on chessboard, return places can be placed chess
    def trace_neighbor(self, chessboard, pos):
        # check all positions in the same row / column / diagonal
        # find the nearest position which is in the same color, add it into neighbor list
        neighbor_list = []

        # column_down
        target_row = pos[0] + 1
        target_col = pos[1]
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_row = target_row + 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # column_up
        target_row = pos[0] - 1
        target_col = pos[1]
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_row = target_row - 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # row_right
        target_row = pos[0]
        target_col = pos[1] + 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_col = target_col + 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # row_left
        target_row = pos[0]
        target_col = pos[1] - 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_col = target_col - 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_right_down
        target_row = pos[0] + 1
        target_col = pos[1] + 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_row = target_row + 1
                target_col = target_col + 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_right_up
        target_row = pos[0] - 1
        target_col = pos[1] + 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_row = target_row - 1
                target_col = target_col + 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_left_down
        target_row = pos[0] + 1
        target_col = pos[1] - 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_row = target_row + 1
                target_col = target_col - 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_right_up
        target_row = pos[0] - 1
        target_col = pos[1] - 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if chessboard[target_row][target_col] == COLOR_NONE:
                break
            elif chessboard[target_row][target_col] != self.color:
                target_row = target_row - 1
                target_col = target_col - 1
                pass_enemy_flag = 1
            elif chessboard[target_row][target_col] == self.color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        return neighbor_list

    def find_candidate(self, neighbor_dict, chessboard, idx):
        for pos in idx:
            neighbor_dict[pos] = self.trace_neighbor(chessboard, pos)

            # check pos valid
            if len(neighbor_dict[pos]) != 0:
                self.candidate_list.append(pos)

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()

        # ==================================================================
        # Write your algorithm here
        # Here is the simplest sample:Random decision
        # row : idx[0], column : idx[1]
        # idx : all empty space in chess board
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
        start = time.time()
        neighbor_dict = {}      # 维护一个字典存放： 位置坐标 -> 附近的邻居列表

        # 遍历棋盘，进行基本的位置搜寻和信息提取
        self.find_candidate(neighbor_dict, chessboard, idx)

        runtime = (time.time() - start)
