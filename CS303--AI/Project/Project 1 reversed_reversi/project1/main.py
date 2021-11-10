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
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

timeout_flag = False
endgame_flag = False
start_time = 0


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
        possible_pos = []
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        for p in idx:
            end = False
            for direct in DIR:
                if end:
                    break
                x, y = p[0] + direct[0], p[1] + direct[1]
                can_reverse = False
                while 0 <= x < self.chessboard_size and 0 <= y < self.chessboard_size:
                    if can_reverse and chessboard[x][y] == cur_player_color:
                        possible_pos.append(p)
                        end = True
                        break
                    elif chessboard[x][y] == -cur_player_color:
                        can_reverse = True
                    else:
                        break
                    x = direct[0] + x
                    y = direct[1] + y
        return possible_pos

    def evaluate(self, cur_state):

        def map_weight_sum(cur_board_state):
            value_map = np.array([[-1000, 200, -60, -60, -60, -60, 200, -1000],
                                  [200, 500, 5, 5, 5, 5, 500, 200],
                                  [-60, 5, 3, 2, 2, 3, 5, -60],
                                  [-60, 5, 2, 1, 1, 2, 5, -60],
                                  [-60, 5, 2, 1, 1, 2, 5, -60],
                                  [-60, 5, 3, 2, 2, 3, 5, -60],
                                  [200, 500, 5, 5, 5, 5, 500, 200],
                                  [-1000, 200, -60, -60, -60, -60, 200, -1000]])
            return sum(sum(cur_board_state * value_map)) * self.color

        def mobility_sum(cur_chessboard_state, tar_player_color):
            candidate_list = self.search_candidate(cur_chessboard_state, tar_player_color)
            return 5 * len(candidate_list)

        def stability_sum(cur_chessboard_state, tar_player_color):
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
            # 遍历四个角
            for i in range(4):
                tar_pos = [corner_row[i], corner_col[i]]
                for j in range(1, self.chessboard_size + 1):
                    for k in range(1, self.chessboard_size + 1):
                        if cur_chessboard_state[tar_pos[0]][tar_pos[1]] == tar_player_color:
                            stability[CORNER] += 1
                            tar_pos = [tar_pos[0] + inc_1[i], tar_pos[1] + inc_2[i]]
                        else:
                            break
                    tar_pos = [corner_row[i] + inc_1[(i + 1) % 4] * j, corner_col[i] + inc_2[(i + 1) % 4] * j]

            # 寻找内部子，即8个方向全部满员的棋子
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
                for k in range(j_range):
                    dig_sum += abs(cur_chessboard_state[start_ind_1 - k][start_ind_2 + k])
                if dig_sum == j_range:
                    for k in range(j_range):
                        dig1_full[start_ind_1 - k][start_ind_2 + k] = True
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
                for k in range(j_range):
                    dig_sum += abs(cur_chessboard_state[start_ind_1 - k][start_ind_2 - k])
                if dig_sum == j_range:
                    for k in range(j_range):
                        dig2_full[start_ind_1 - k][start_ind_2 - k] = True
            stability[INNER] = sum(
                sum(np.logical_and(np.logical_and(np.logical_and(col_full, row_full), dig1_full), dig2_full)))

            final_stability = stability[CORNER] + stability[BORDER] + stability[INNER]
            return final_stability

        my_mobility = mobility_sum(cur_state, self.color)
        enemy_mobility = mobility_sum(cur_state, -self.color)

        my_stability = stability_sum(cur_state, self.color)
        enemy_stability = stability_sum(cur_state, -self.color)

        value = map_weight_sum(cur_state) + 5 * (my_mobility - enemy_mobility) + 15 * (enemy_stability - my_stability)
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

    def alpha_beta(self, cur_chessboard):
        global timeout_flag
        global endgame_flag
        global start_time

        def max_value(cur_state, alpha, beta, avail_pos, left_depth):
            global timeout_flag
            global endgame_flag
            if time.time() - start_time > self.time_out - 0.7:
                timeout_flag = True
                return +infinity, None
            if left_depth == 0:
                return self.evaluate(cur_state), None

            value, best_move = -infinity, None
            for candidate_pos in avail_pos:
                next_state = self.actions(copy.deepcopy(cur_state), candidate_pos, self.color)
                next_avail = self.search_candidate(next_state, -self.color)
                if next_avail:
                    next_state_value, _ = min_value(next_state, alpha, beta, copy.deepcopy(next_avail), left_depth - 1)
                else:
                    next_avail = self.search_candidate(next_state, self.color)
                    if next_avail:
                        next_state_value, _ = max_value(next_state, alpha, beta, copy.deepcopy(next_avail), left_depth - 1)
                    else:
                        timeout_flag = time.time() - start_time > self.time_out - 0.7
                        next_state_value = +infinity * (np.count_nonzero(cur_state == -self.color) - np.count_nonzero(
                            cur_state == self.color))
                        endgame_flag = True
                        if next_state_value == +infinity:
                            return next_state_value, candidate_pos
                if timeout_flag:
                    break
                if next_state_value > value:
                    value, best_move = next_state_value, candidate_pos
                    alpha = max(alpha, value)
                if value >= beta:
                    return value, best_move
            return value, best_move

        def min_value(cur_state, alpha, beta, avail_pos, left_depth):
            global timeout_flag
            global endgame_flag
            if time.time() - start_time > self.time_out - 0.7:
                timeout_flag = True
                return +infinity, None
            if left_depth == 0:
                return self.evaluate(cur_state), None

            value, best_move = +infinity, None
            for candidate_pos in avail_pos:
                next_state = self.actions(copy.deepcopy(cur_state), candidate_pos, -self.color)
                next_avail = self.search_candidate(next_state, self.color)
                if next_avail:
                    next_state_value, _ = max_value(next_state, alpha, beta, copy.deepcopy(next_avail), left_depth - 1)
                else:
                    next_avail = self.search_candidate(next_state, -self.color)
                    if next_avail:
                        next_state_value, _ = min_value(next_state, alpha, beta, copy.deepcopy(next_avail), left_depth - 1)
                    else:
                        timeout_flag = time.time() - start_time > self.time_out - 0.7
                        next_state_value = +infinity * (np.count_nonzero(cur_state == -self.color) - np.count_nonzero(cur_state == self.color))
                        endgame_flag = True
                        if next_state_value == -infinity:
                            return next_state_value, candidate_pos
                if timeout_flag:
                    break
                if next_state_value < value:
                    value, best_move = next_state_value, candidate_pos
                    beta = min(beta, value)
                if value <= alpha:
                    return value, best_move
            return value, best_move

        if self.candidate_list:
            depth = 3
            while not timeout_flag and not endgame_flag:
                _, move = max_value(cur_chessboard, -infinity, +infinity, copy.deepcopy(self.candidate_list), depth)
                if move:
                    self.candidate_list.append(move)
                depth += 1

    # The input is current chessboard.
    def go(self, chessboard):
        global start_time
        global timeout_flag
        global endgame_flag
        timeout_flag = False
        endgame_flag = False
        start_time = time.time()
        self.candidate_list.clear()
        self.candidate_list = self.search_candidate(chessboard, self.color)
        self.alpha_beta(chessboard)


if __name__ == "__main__":
    log = np.array([[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, -1, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, -1, 1, -1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, -1, -1, -1, 0, 0], [0, 0, 0, 0, -1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, -1, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, -1, -1, 1, 0, 0], [0, 0, 0, 0, -1, -1, 0, 0],
                     [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, -1, -1, 0, 0],
                     [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, -1, 0], [0, 0, 0, 1, 1, -1, 0, 0], [0, 0, 0, 1, -1, -1, 0, 0],
                     [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, -1, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, -1, 0], [0, 0, 0, 1, 1, -1, 0, 0], [0, 0, 0, 1, -1, 1, 1, 0],
                     [0, 0, 0, -1, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, -1, 0], [0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, -1, 1, 1, 0],
                     [0, 0, 0, -1, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                     [0, 0, 0, -1, 1, 1, -1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, -1, 1, 1, 0],
                     [0, 0, 0, -1, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                     [0, 0, 0, -1, 1, 1, -1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0],
                     [0, 0, 0, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                     [0, 0, 0, -1, 1, 1, -1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0],
                     [0, 0, 0, -1, 0, 0, -1, 0], [0, 0, 1, -1, 0, 0, 0, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                     [0, 0, 0, -1, 1, 1, -1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0],
                     [0, 0, 0, -1, 0, 0, 1, 0], [0, 0, 1, -1, 0, 0, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0],
                     [0, 0, 0, -1, 1, 1, -1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, -1, -1, -1, -1],
                     [0, 0, 0, -1, 0, 0, 1, 0], [0, 0, 1, -1, 0, 0, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, -1, -1, -1, -1],
                     [0, 0, 0, -1, 0, 0, 1, 0], [0, 0, 1, -1, 0, 0, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, -1, -1, -1, -1],
                     [0, 0, 0, -1, 0, 0, 1, 0], [0, -1, -1, -1, 0, 0, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, -1, -1, 1, -1],
                     [0, 0, 0, -1, 0, 0, 1, 1], [0, -1, -1, -1, 0, 0, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, -1, -1, 1, -1],
                     [0, 0, 0, -1, 0, 0, -1, 1], [0, -1, -1, -1, 0, -1, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, 1, 1, 1, 0], [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, 0, -1, 1], [0, -1, -1, -1, 0, -1, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, -1, 1, 1, -1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, 0, -1, 1], [0, -1, -1, -1, 0, -1, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, -1, 1, 1, -1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, 0, -1, 1], [0, -1, -1, -1, 1, 1, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, -1, 0, 0, 0, -1],
                     [0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, -1, 1, 1, -1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, 0, -1, 1], [0, -1, -1, -1, 1, 1, 1, 0]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, -1, 0, 0, 0, -1],
                     [0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, -1, 1, 1, -1, 1], [0, 0, 0, -1, -1, 1, 1, 1],
                     [0, 0, 0, -1, 0, 0, 1, 1], [0, -1, -1, -1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, -1, 0, 0, 0, -1],
                     [0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, -1, 1, -1, -1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, -1, 1, 1], [0, -1, -1, -1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, 0, 0, 1],
                     [0, 0, 0, -1, -1, -1, -1, 1], [0, 0, 0, -1, 1, -1, -1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, -1, 1, 1], [0, -1, -1, -1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, 0, 1, 1],
                     [0, 0, 0, -1, -1, 1, 1, 1], [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, -1, 1, 1], [0, -1, -1, -1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, -1, 1, 1],
                     [0, 0, 0, -1, -1, -1, 1, 1], [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, -1, 1, 1], [0, -1, -1, -1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, -1, 1, 1],
                     [0, 0, 0, -1, -1, -1, 1, 1], [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, 0, -1, -1, -1, 1, 1],
                     [0, 0, 0, -1, 0, -1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, -1, 1, 1],
                     [0, 0, 0, -1, -1, -1, 1, 1], [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, 0, 1, -1, -1, 1, 1],
                     [0, 0, 1, -1, 0, -1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, -1, 1, 1],
                     [0, 0, 0, -1, -1, -1, 1, 1], [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, -1, -1, -1, -1, 1, 1],
                     [0, 0, 1, -1, 0, -1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, -1, 1, 1],
                     [0, 0, 0, -1, -1, -1, 1, 1], [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, -1, -1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, -1, 1, 1],
                     [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, -1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, -1, 0, 0, 0, 1], [0, 0, 0, -1, 0, -1, 1, 1],
                     [0, 0, 0, -1, 1, -1, 1, 1], [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, -1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, -1, 0, 1, 0, 1], [0, 0, 0, -1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, -1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, -1, -1, -1, 0, 1, 0, 1], [0, 0, 0, -1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, -1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, -1, -1, -1, 0, 1, 0, 1], [0, 0, 0, -1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 1], [0, -1, -1, -1, 0, 1, 0, 1], [0, 0, 0, -1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 0, 0, 0, 0, 1], [0, -1, 1, -1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [0, -1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [0, -1, -1, -1, -1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 0, 0, -1, 1, 1, 1, 1], [0, 0, -1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 1, 0, -1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 1, 0, -1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 1, 0, -1, 1, 1, 1, 1], [1, 0, -1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [-1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1],
                     [0, 1, 0, -1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [-1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, -1, 0, 1, 0, 1, 1, 1],
                     [0, -1, 0, -1, 1, 1, 1, 1], [1, -1, 1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [-1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, -1, 0, 1, 0, 1, 1, 1],
                     [0, 1, 0, -1, 1, 1, 1, 1], [1, -1, 1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [-1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1],
                     [1, 1, 0, -1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, -1, 1, 1, 1, 1, 1, 1],
                     [-1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1],
                     [1, 1, 0, -1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1],
                     [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]])
    tar_chessboard = np.array([[1, 1, 1, -1, -1, -1, 1, -1],
                               [1, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 1, -1, 0, 0, 0],
                               [0, 0, 0, -1, -1, 0, 0, 0],
                               [0, 0, 0, 1, -1, 0, 0, 0],
                               [1, 0, 0, 1, 0, 0, 0, 0],
                               [0, 1, 0, 1, 0, 0, 0, 0]])
    a = time.time()
    ai = AI(8, COLOR_WHITE, 5)
    # ai.evaluate(log[13])
    print(log[22])
    ai.go(log[22])
    print(ai.candidate_list)
    print(time.time() - a)
