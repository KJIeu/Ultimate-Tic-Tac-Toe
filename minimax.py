import numpy as np

from check_game import get_possible_moves, validate_box, is_empty_box
from check_game import set_locations
from check_game import empty_cells_small_boards, empty_cells_big_board, \
    check_big_board
import copy


def minimax(board, main_board, depth, box, player, maximizing_player):
    if depth == 0 or is_terminal(board, main_board, box, player):
        return board, evaluate(board, player), None

    if maximizing_player:
        max_value = -np.inf
        best_board = None
        pos = None
        all_boards, all_big_boards, all_boxes, positions = get_all_moves(board, main_board, box, player)

        for board_, main_board_, box_, pos_ in zip(all_boards, all_big_boards,
                                                   all_boxes, positions):
            #value = minimax(board_, main_board_, depth - 1, box_, -player, True)[1]
            value = minimax(board_, main_board_, depth - 1, box_, -player, False)[1]
            max_value = max(max_value, value)
            if max_value == value:
                best_board = board_

                pos = pos_

        #print(best_board, max_value, pos)
        return best_board, max_value, pos
    else:
        min_value = float('inf')
        best_board = None
        pos = None
        all_boards, all_big_boards, all_boxes, positions = get_all_moves(board,
                                                                         main_board,
                                                                         box,
                                                                         player)
        for board_, main_board_, box_, pos_ in zip(all_boards, all_big_boards,
                                                   all_boxes, positions):
            #value = minimax(board_, main_board_, depth - 1, box_, -player, False)[1]
            value = minimax(board_, main_board_, depth - 1, box_, -player, True)[1]
            min_value = min(min_value, value)
            if min_value == value:
                best_board = board_
                pos = pos_
        #print(best_board, min_value, pos)
        return best_board, min_value, pos


def evaluate(board, player):
    score = get_score(board, player)
    return score


def get_score(board, player):
    score = 0
    for i in range(0, 9, 3):
        box = []
        for j in range(0, 9, 3):
            for h in range(3):
                temp_list = []
                for k in range(3):
                    temp_list.append(board[h + i][j + k])
                box.append(temp_list)
            score += eval_box(box, player)
            box.clear()
    #print(score)
    return score


def eval_box(box, player):
    score = 0
    for row in box:  # Score for each row
        score += count_score(row, player)
    #score = np.

    for col in range(len(box)):  # Score for each column
        check = []
        for _ in box:
            check.append(box[col])

        score += count_score(box, player)

    # A score for each diagonal
    diags = []
    #for idx in range(len(box)):
        #diags.append(box[idx][idx])
    diags = np.diag(box)

    score += count_score(diags, player)

    diags_2 = []
    for idx, rev_idx in enumerate(reversed(range(len(box)))):
        diags_2.append(box[idx][rev_idx])
    score += count_score(diags_2, player)

    if len(empty_cells_small_boards(box)) == 0:
        score += 1
    #print(score)
    return score


def count_score(array, player):
    opp_player = -player
    score = 0

    if array.count(player) == 3:
        score += 1000

    elif array.count(player) == 2:
        score += 100

    elif array.count(player) == 1:
        score += 20

    if array.count(opp_player) == 3:
        score -= 1000

    elif array.count(opp_player) == 2:
        score -= 100

    if array.count(player) == 1 and array.count(opp_player) == 2:
        score -= 20

    return score


def get_all_moves(board, main_board, box, player):
    all_boards = []
    all_big_boards = []
    all_boxes = []
    all_pos = []
    if box is None:
        for idx, pos in enumerate(empty_cells_small_boards(board)):
            new_board = copy.deepcopy(board)
            new_main_board = copy.deepcopy(main_board)
            x = pos[0]
            y = pos[1]

            if set_locations(new_board, new_main_board, x, y, player, box):
                all_boards.append(new_board)
                all_big_boards.append(new_main_board)
                box_ = get_possible_moves(new_board, x, y)
                new_box = validate_box(new_board, new_main_board, box_, x, y)
                all_boxes.append(new_box)
                all_pos.append(pos)

        return all_boards, all_big_boards, all_boxes, all_pos

    else:
        for idx, pos in enumerate(box):
            new_board = copy.deepcopy(board)
            new_main_board = copy.deepcopy(main_board)
            x = pos[0]
            y = pos[1]

            if set_locations(new_board, new_main_board, x, y, player, box):
                all_boards.append(new_board)
                all_big_boards.append(new_main_board)
                box_ = get_possible_moves(new_board, x, y)
                new_box = validate_box(new_board, new_main_board, box_, x, y)
                all_boxes.append(new_box)
                all_pos.append(pos)

        return all_boards, all_big_boards, all_boxes, all_pos


def is_terminal(board, main_board, box, player):
    if len(empty_cells_small_boards(board)) == 0:
        return True

    if len(empty_cells_big_board(main_board)) == 0:
        return True

    if check_big_board(main_board, player):
        return True

    """
    if not is_empty_box(Board, Main_board, Box):
        print("empty box true")
        return True

    """
