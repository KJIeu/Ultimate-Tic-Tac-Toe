import numpy as np

from check_game import empty_cells_small_boards
from minimax import get_all_moves, count_score, is_terminal


def minimax_alpha_beta(board, main_board, depth, box, player, maximizing_player, alpha=-np.inf, beta=np.inf):
    if depth == 0 or is_terminal(board, main_board, box, player):
        return board, evaluate(board, player), None

    if maximizing_player:
        max_value = -np.inf
        best_board = None
        pos = None
        all_boards, all_big_boards, all_boxes, positions = get_all_moves(board, main_board, box, player)

        for board_, main_board_, box_, pos_ in zip(all_boards, all_big_boards, all_boxes, positions):
            value = minimax_alpha_beta(board_, main_board_, depth - 1, box_, -player, False, alpha, beta)[1]
            if value > max_value:
                max_value = value
                best_board = np.copy(board_)
                pos = pos_

            alpha = max(alpha, max_value)
            if alpha >= beta:
                break

        return best_board, max_value, pos

    else:
        min_value = np.inf
        best_board = None
        pos = None
        all_boards, all_big_boards, all_boxes, positions = get_all_moves(board, main_board, box, player)

        for board_, main_board_, box_, pos_ in zip(all_boards, all_big_boards, all_boxes, positions):
            value = minimax_alpha_beta(board_, main_board_, depth - 1, box_, -player, True, alpha, beta)[1]
            if value < min_value:
                min_value = value
                best_board = np.copy(board_)
                pos = pos_

            beta = min(beta, min_value)
            if beta <= alpha:
                break

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
    return score


def eval_box(box, player):
    score = 0
    for row in box:  # Score for each row
        score += count_score(row, player)

    for col in range(len(box)):  # Score for each column
        check = []
        for _ in box:
            check.append(box[col])

        score += count_score(box, player)

    # A score for each diagonal
    diags = []
    for idx in range(len(box)):
        diags.append(box[idx][idx])


    score += count_score(diags, player)

    diags_2 = []
    for idx, rev_idx in enumerate(reversed(range(len(box)))):
        diags_2.append(box[idx][rev_idx])
    score += count_score(diags_2, player)

    if len(empty_cells_small_boards(box)) == 0:
        score += 10
    #print(score)
    return score


