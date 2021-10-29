import numpy as np
import copy
import random
import math
import time

infinity = math.inf

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

    def trace_neighbor(self, cur_state, target_pos, cur_player_color):
        # check all positions in the same row / column / diagonal
        # find the nearest position which is in the same color, add it into neighbor list
        neighbor_list = []

        # column_down
        target_row = target_pos[0] + 1
        target_col = target_pos[1]
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_row = target_row + 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # column_up
        target_row = target_pos[0] - 1
        target_col = target_pos[1]
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_row = target_row - 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # row_right
        target_row = target_pos[0]
        target_col = target_pos[1] + 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_col = target_col + 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # row_left
        target_row = target_pos[0]
        target_col = target_pos[1] - 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_col = target_col - 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_right_down
        target_row = target_pos[0] + 1
        target_col = target_pos[1] + 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_row = target_row + 1
                target_col = target_col + 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_right_up
        target_row = target_pos[0] - 1
        target_col = target_pos[1] + 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_row = target_row - 1
                target_col = target_col + 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_left_down
        target_row = target_pos[0] + 1
        target_col = target_pos[1] - 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_row = target_row + 1
                target_col = target_col - 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        # diagonal_right_up
        target_row = target_pos[0] - 1
        target_col = target_pos[1] - 1
        pass_enemy_flag = -1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if cur_state[target_row][target_col] == COLOR_NONE:
                break
            elif cur_state[target_row][target_col] != cur_player_color:
                target_row = target_row - 1
                target_col = target_col - 1
                pass_enemy_flag = 1
            elif cur_state[target_row][target_col] == cur_player_color and pass_enemy_flag == 1:
                neighbor_list.append((target_row, target_col))
                break
            else:
                break

        return neighbor_list

    def search_candidate(self, chessboard, cur_player_color):
        # row : idx[0], column : idx[1]
        # idx : all empty space in chess board
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        neighbor_dict = {}
        candidate_list = []
        for pos in idx:
            neighbor_dict[pos] = self.trace_neighbor(chessboard[:], pos, cur_player_color)
            if len(neighbor_dict[pos]) != 0:
                candidate_list.append(pos)
        return neighbor_dict, candidate_list

    def terminal_test(self, cur_chessboard_state):
        # 双方都没地方落子游戏结束
        _, candidate_list_1 = self.search_candidate(cur_chessboard_state, self.color)
        _, candidate_list_2 = self.search_candidate(cur_chessboard_state, -self.color)
        return len(candidate_list_1) == 0 and len(candidate_list_2) == 0

    def evaluate(self, cur_state):

        def map_weight_sum(cur_board_state):
            value_map = np.array([[-500, 25, -10, -5, -5, -10, 25, -500],
                                  [25, 45, -1, -1, -1, -1, 45, 25],
                                  [-10, -1, -3, -2, -2, -3, -1, -10],
                                  [-5, -1, -2, -1, -1, -2, -1, -5],
                                  [-5, -1, -2, -1, -1, -2, -1, -5],
                                  [-10, -1, -3, -2, -2, -3, -1, -10],
                                  [25, 45, -1, -1, -1, -1, 45, 25],
                                  [-500, 25, -10, -5, -5, -10, 25, -500]])
            return sum(sum(cur_board_state * value_map)) * self.color

        def mobility_sum(cur_chessboard_state, cur_player_color):
            _, candidate_list_1 = self.search_candidate(cur_chessboard_state[:], cur_player_color)
            return len(candidate_list_1)

        def stability_sum(cur_chessboard_state, cur_player_color):
            max_length = self.chessboard_size - 1
            CORNER = 0
            BORDER = 1
            INNER = 2
            stability = [0, 0, 0]

            # 四个角：左上， 右上， 右下， 左下
            corner_row = [0, 0, max_length, max_length]
            corner_col = [0, max_length, max_length, 0]
            # 移动方向：向右， 向下， 向左， 向上
            inc_1 = [0, 1, 0, -1]
            inc_2 = [1, 0, -1, 0]
            # 分别有多少连续的己方子在自己的移动方向上
            stop = [0, 0, 0, 0]
            for i in range(4):
                if cur_chessboard_state[corner_row[i]][corner_col[i]] == cur_player_color:
                    stop[i] = 1
                    stability[CORNER] += 1
                    for j in range(1, max_length):
                        if cur_chessboard_state[corner_row[i] + inc_1[i] * j][corner_col[i] + inc_2[i] * j] != cur_player_color:
                            break
                        else:
                            stop[i] = j + 1
                            stability[BORDER] += 1
                    for j in range(1, max_length - stop[i - 1]):
                        if cur_chessboard_state[corner_row[i] - inc_1[i - 1] * j][corner_col[i] - inc_2[i - 1] * j] != cur_player_color:
                            break
                        else:
                            stability[BORDER] += 1

            col_full = np.zeros((self.chessboard_size, self.chessboard_size), dtype=int)
            col_full[:, np.sum(abs(cur_chessboard_state), axis=0) == self.chessboard_size] = True

            row_full = np.zeros((self.chessboard_size, self.chessboard_size), dtype=int)
            row_full[np.sum(abs(cur_chessboard_state), axis=1) == self.chessboard_size, :] = True

            dig1_full = np.zeros((self.chessboard_size, self.chessboard_size), dtype=int)
            for i in range(15):
                dig_sum = 0
                if i <= max_length:
                    start_ind_1 = i
                    start_ind_2 = 0
                    j_range = i + 1
                else:
                    start_ind_1 = max_length
                    start_ind_2 = i - max_length
                    j_range = 15 - i
                for j in range(j_range):
                    dig_sum += abs(cur_chessboard_state[start_ind_1 - j][start_ind_2 + j])
                if dig_sum == j_range:
                    for k in range(j_range):
                        dig1_full[start_ind_1 - j][start_ind_2 + j] = True

            dig2_full = np.zeros((self.chessboard_size, self.chessboard_size), dtype=int)
            for i in range(15):
                dig_sum = 0
                if i <= 7:
                    start_ind_1 = i
                    start_ind_2 = 7
                    j_range = i + 1
                else:
                    start_ind_1 = 7
                    start_ind_2 = 14 - i
                    j_range = 15 - i
                for j in range(j_range):
                    dig_sum += abs(cur_chessboard_state[start_ind_1 - j][start_ind_2 - j])
                if dig_sum == j_range:
                    for k in range(j_range):
                        dig2_full[start_ind_1 - j][start_ind_2 - j] = True
            stability[2] = sum(sum(np.logical_and(np.logical_and(np.logical_and(col_full, row_full), dig1_full), dig2_full)))
            return stability

        my_mobility = mobility_sum(cur_state[:], self.color)
        enemy_mobility = mobility_sum(cur_state[:], self.color)
        my_stability = stability_sum(cur_state[:], self.color)
        value = map_weight_sum(cur_state) + 15 * (my_mobility - enemy_mobility) + (-10) * sum(my_stability)
        return int(value)

    def actions(self, next_state, target_pos, cur_player):
        next_state[target_pos[0]][target_pos[1]] = cur_player

        # column_down
        target_row = target_pos[0] + 1
        target_col = target_pos[1]
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_row = target_row + 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # column_up
        target_row = target_pos[0] - 1
        target_col = target_pos[1]
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_row = target_row - 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # row_right
        target_row = target_pos[0]
        target_col = target_pos[1] + 1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_col = target_col + 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # row_left
        target_row = target_pos[0]
        target_col = target_pos[1] - 1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_col = target_col - 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # diagonal_right_down
        target_row = target_pos[0] + 1
        target_col = target_pos[1] + 1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_row = target_row + 1
                target_col = target_col + 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # diagonal_right_up
        target_row = target_pos[0] - 1
        target_col = target_pos[1] + 1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_row = target_row - 1
                target_col = target_col + 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # diagonal_left_down
        target_row = target_pos[0] + 1
        target_col = target_pos[1] - 1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_row = target_row + 1
                target_col = target_col - 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        # diagonal_right_up
        target_row = target_pos[0] - 1
        target_col = target_pos[1] - 1
        while (self.chessboard_size - 1 >= target_row >= 0) and (self.chessboard_size - 1 >= target_col >= 0):
            if next_state[target_row][target_col] == -cur_player:
                next_state[target_row][target_col] = cur_player
                target_row = target_row - 1
                target_col = target_col - 1
            elif next_state[target_row][target_col] == cur_player:
                break
            else:
                break

        return next_state

    def alpha_beta(self, cur_chessboard, cutoff):

        def max_value(cur_state, alpha, beta, depth):
            if depth >= cutoff:
                return self.evaluate(cur_state[:]), None

            if self.terminal_test(cur_state):
                return self.evaluate(cur_state[:]), None

            value, move = -infinity, None

            _, candidate_list = self.search_candidate(cur_state, self.color)
            for candidate_pos in candidate_list:
                next_state = copy.deepcopy(cur_state)
                next_state = self.actions(next_state, candidate_pos, self.color)
                next_state_value, _ = min_value(next_state, alpha, beta, depth + 1)
                if next_state_value > value:
                    value, move = next_state_value, candidate_pos
                    alpha = max(alpha, value)
                if value >= beta:
                    return value, move

            return value, move

        def min_value(cur_state, alpha, beta, depth):
            if depth >= cutoff:
                return self.evaluate(cur_state[:]), None

            if self.terminal_test(cur_state):
                return self.evaluate(cur_state[:]), None

            value, move = +infinity, None

            _, candidate_list = self.search_candidate(cur_state, -self.color)
            for candidate_pos in candidate_list:
                next_state = copy.deepcopy(cur_state)
                next_state = self.actions(next_state, candidate_pos, -self.color)
                next_state_value, _ = max_value(next_state, alpha, beta, depth + 1)
                if next_state_value < value:
                    value, move = next_state_value, candidate_pos
                    beta = min(beta, value)
                if value <= alpha:
                    return value, move

            return value, move

        return max_value(cur_chessboard, -infinity, +infinity, 0)

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()

        # candidate_list example: [pos1, pos2, ...]
        # pos example:  (row_number, col_number)
        start = time.time()

        # 遍历棋盘，进行基本的位置搜寻和信息提取
        # 维护一个字典存放： 位置坐标 -> 附近的邻居列表
        neighbor_dict, self.candidate_list = self.search_candidate(chessboard, self.color)
        target_depth = 4
        runtime = (time.time() - start)
        while runtime < self.time_out / 4:
            _, move = self.alpha_beta(chessboard, target_depth)
            target_depth = target_depth + 1
            if move is not None:
                self.candidate_list.append(move)
            runtime = (time.time() - start)


if __name__ == "__main__":
    log = np.array([[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,1,-1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,-1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,-1,-1,-1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,1,1,1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,-1,1,0,0,0],[0,1,1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,0,1,1,0,0,0],[0,1,1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,-1,0,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0],[0,1,0,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,-1,0,0,0,0],[0,1,1,-1,0,0,0,0],[0,1,0,-1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,1,-1,0,0,0,0],[0,1,1,1,0,0,0,0],[0,1,0,-1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,-1,-1,-1,0,0,0,0],[0,1,-1,1,0,0,0,0],[0,1,0,-1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,-1,-1,-1,0,0,0,0],[0,1,-1,1,0,0,0,0],[0,1,1,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,0,0,0,0],[0,-1,-1,1,0,0,0,0],[0,1,-1,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,0,0,0,0],[1,1,1,1,0,0,0,0],[0,1,-1,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,0,0,0],[1,1,1,-1,0,0,0,0],[0,1,-1,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,0,0,0],[1,1,1,1,1,0,0,0],[0,1,-1,1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,0,0],[1,1,1,1,-1,0,0,0],[0,1,-1,-1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,0,0],[1,1,1,1,1,1,0,0],[0,1,-1,-1,1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,1,-1,0,0],[0,1,-1,-1,-1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,1,1,1,0],[0,1,-1,-1,-1,0,0,0],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,1,1,-1,0],[0,1,-1,-1,-1,0,0,-1],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,1,1,1,1],[0,1,-1,-1,-1,0,0,-1],[0,1,-1,-1,1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,-1,-1,1,1],[0,1,-1,-1,-1,-1,0,-1],[0,1,-1,-1,-1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,-1,-1,1,1],[0,1,1,1,1,1,1,-1],[0,1,-1,-1,-1,1,0,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,-1,-1,-1,1],[0,1,1,1,1,-1,-1,-1],[0,1,-1,-1,-1,-1,-1,0],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,1,1,-1,-1,-1,1],[0,1,1,1,1,-1,-1,1],[0,1,1,1,1,1,1,1],[0,0,0,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,0],[1,1,-1,1,-1,-1,-1,1],[0,1,-1,1,-1,-1,-1,1],[0,1,-1,-1,1,1,1,1],[0,0,-1,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[1,1,-1,1,-1,-1,1,1],[0,1,-1,1,-1,1,-1,1],[0,1,-1,-1,1,1,1,1],[0,0,-1,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[1,1,-1,1,-1,-1,1,1],[0,-1,-1,1,-1,1,-1,1],[-1,-1,-1,-1,1,1,1,1],[0,0,-1,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[1,1,-1,1,-1,-1,1,1],[1,1,1,1,-1,1,-1,1],[-1,-1,-1,-1,1,1,1,1],[0,0,-1,-1,-1,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[1,1,-1,1,-1,-1,1,1],[1,1,1,1,-1,1,-1,1],[-1,-1,-1,-1,1,-1,-1,1],[0,0,-1,-1,-1,0,-1,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[1,1,-1,1,-1,-1,1,1],[1,1,1,1,-1,1,-1,1],[1,1,-1,-1,1,-1,-1,1],[1,0,-1,-1,-1,0,-1,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,1,-1,1,-1,-1,1,1],[-1,1,1,1,-1,1,-1,1],[-1,1,-1,-1,1,-1,-1,1],[-1,0,-1,-1,-1,0,-1,0],[-1,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,1,-1,1,-1,-1,1,1],[-1,1,1,1,-1,1,-1,1],[-1,1,1,-1,1,-1,-1,1],[-1,1,-1,-1,-1,0,-1,0],[-1,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,-1,-1,-1,0,-1,0],[-1,-1,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,1,-1,1],[-1,-1,1,-1,1,1,1,1],[-1,-1,-1,-1,-1,1,-1,0],[-1,-1,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,-1,-1,-1,-1,0],[-1,-1,0,0,-1,-1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,1,1,-1,-1,-1,0],[-1,-1,1,0,-1,-1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,-1,-1,-1,-1,0],[-1,-1,-1,-1,-1,-1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,-1,-1,1,1,0],[-1,-1,-1,-1,-1,-1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,-1,-1,1,-1,0],[-1,-1,-1,-1,-1,-1,-1,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,-1,-1,1,1,1],[-1,-1,-1,-1,-1,-1,-1,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,1,-1,1,1,1],[-1,-1,1,-1,-1,-1,-1,-1],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,1,-1,1,1,1],[-1,-1,-1,-1,-1,-1,-1,-1],[0,1,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,1,-1,1,1,1],[-1,-1,-1,1,1,-1,-1,-1],[0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,1,-1,1,1,1],[-1,-1,-1,-1,-1,-1,-1,-1],[0,1,1,1,-1,0,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,1,1],[-1,-1,-1,1,-1,1,1,1],[-1,-1,-1,-1,1,1,1,-1],[0,1,1,1,1,1,0,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,-1,1,-1,1,-1,1],[-1,-1,-1,-1,1,-1,-1,-1],[0,1,1,1,1,1,-1,0],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,-1,1,-1,1,-1,1],[-1,-1,-1,-1,1,-1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,-1,1,-1,1,-1,1],[-1,-1,-1,-1,1,-1,1,1],[0,-1,1,1,1,1,1,1],[-1,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,-1,1,-1,1,-1,1],[-1,-1,-1,-1,1,-1,1,1],[1,1,1,1,1,1,1,1],[-1,0,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,-1,1,-1,1,-1,1],[-1,-1,-1,-1,1,-1,1,1],[1,-1,-1,1,1,1,1,1],[-1,-1,0,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,1,1,-1,1,-1,1],[-1,-1,1,-1,1,-1,1,1],[1,-1,1,1,1,1,1,1],[-1,-1,1,0,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,1,1,-1,1,-1,1],[-1,-1,1,-1,1,-1,1,1],[1,-1,-1,-1,-1,1,1,1],[-1,-1,-1,-1,0,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,1,-1,1,-1,-1,1],[-1,-1,1,1,-1,1,-1,1],[-1,-1,1,-1,1,-1,1,1],[1,-1,-1,1,1,1,1,1],[-1,-1,-1,-1,1,0,0,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,-1,-1,1,-1,-1,1],[-1,-1,1,-1,-1,1,-1,1],[-1,-1,1,-1,-1,-1,-1,1],[1,-1,-1,1,1,-1,-1,1],[-1,-1,-1,-1,1,0,-1,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,-1,-1,1,-1,-1,1],[-1,-1,1,-1,-1,1,-1,1],[-1,-1,1,-1,-1,1,-1,1],[1,-1,-1,1,1,1,1,1],[-1,-1,-1,-1,1,1,-1,0]],[[-1,-1,-1,-1,-1,-1,-1,1],[-1,-1,-1,1,-1,-1,1,1],[-1,-1,1,1,-1,-1,-1,1],[-1,-1,-1,-1,1,-1,-1,1],[-1,-1,1,-1,-1,1,-1,1],[-1,-1,1,-1,-1,-1,-1,1],[1,-1,-1,1,1,1,-1,1],[-1,-1,-1,-1,1,1,-1,-1]]])
    a = time.time()
    ai = AI(8, COLOR_BLACK, 5)
    print(log[13])
    ai.go(log[13])
    print(ai.candidate_list)
    print(time.time() - a)
