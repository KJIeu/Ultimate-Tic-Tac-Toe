#from frontend import win_window
from frontend import winner


def valid_locations(board, main_board, x, y, box):
    if box is None or [x, y] in box:
        if board[y][x] == 0 and main_board[y // 3][x // 3] == 0:
            return True


def set_locations(board, main_board, x, y, player, box):
    if valid_locations(board, main_board, x, y, box):
        board[y][x] = player
        return True
    else:
        return False


def get_next_box(x, y):
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3):
                    for h in range(3):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(0, 7, 3):
        for j in range(1, 8, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3):
                    for h in range(3, 6):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(0, 7, 3):
        for j in range(2, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3):
                    for h in range(6, 9):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(1, 8, 3):
        for j in range(0, 7, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3, 6):
                    for h in range(3):
                        possible_moves.append([k, h])

                return possible_moves

    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3, 6):
                    for h in range(3, 6):
                        possible_moves.append([k, h])

                return possible_moves

    for i in range(1, 8, 3):
        for j in range(2, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3, 6):
                    for h in range(6, 9):
                        possible_moves.append([k, h])

                return possible_moves

    for i in range(2, 9, 3):
        for j in range(0, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(6, 9):
                    for h in range(3):
                        possible_moves.append([k, h])

                return possible_moves

    for i in range(2, 9, 3):
        for j in range(1, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(6, 9):
                    for h in range(3, 6):
                        possible_moves.append([k, h])

                return possible_moves

    for i in range(2, 9, 3):
        for j in range(2, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(6, 9):
                    for h in range(6, 9):
                        possible_moves.append([k, h])

                return possible_moves


def is_empty_box(Board, main_board, box):
    empty_cells = []
    if box is None:
        return False
    else:
        for index, values in enumerate(box):
            if Board[values[1]][values[0]] == 0:
                empty_cells.append(values)

    if len(empty_cells) == 0:
        return False

    else:
        return True


def get_possible_moves(board, x, y):
    box = get_next_box(x, y)
    return box


def validate_box(board, main_board, box, x, y):
    if is_empty_box(board, main_board, box) and \
            main_board[box[0][1] // 3][box[0][0] // 3] == 0:
        return box
    else:
        return empty_cells_small_boards(board)


def place_big_board(main_board, x, y, player):
    main_board[y][x] = player


def empty_cells_small_boards(board):
    empty_cells = []
    for y, row in enumerate(board):  # Switched y and x. Maybe it will cause issues
        for x, case in enumerate(row):
            if case == 0:
                empty_cells.append([x, y])

    return empty_cells


def empty_cells_big_board(main_board):
    empty_cells = []
    for x, row in enumerate(main_board):
        for y, case in enumerate(row):
            if case == 0:
                empty_cells.append([x, y])

    return empty_cells


def check_horizontally(board, main_board, player):
    good = False
    for i in range(0, 7, 3):
        for idx, row in enumerate(board):
            if row[0 + i] == row[1 + i] == row[2 + i] == player:
                good = True
                if good:
                    place_big_board(main_board, i // 3, idx // 3, player)
                    good = False


def check_vertically(board, main_board, player):
    for idx in range(len(board)):
        check = []
        for i, row in enumerate(board):
            check.append(row[idx])
            if len(check) >= 3:
                if check.count(player) == len(check) and check[0] != 0:
                    good_col = True
                    if good_col:
                        place_big_board(main_board, idx // 3, i // 3, player)
                    else:
                        check.clear()
                else:
                    check.clear()


def check_diagonals(board, main_board, player):
    for x in range(0, 8, 3):
        stock_idx = []
        for y in range(0, 8, 3):
            stock_idx.append(board[y][x])
            for i in range(1, 3):
                stock_idx.append(board[y + i][x + i])
                if len(stock_idx) >= 3:
                    if stock_idx.count(player) == len(stock_idx):
                        a, b = y + i, x + i
                        place_big_board(main_board, b // 3, a // 3, player)
                        stock_idx.clear()
                    else:
                        stock_idx.clear()

    for x in range(0, 9, 3):
        stock_idx = []
        for y in range(2, 9, 3):
            for i in range(3):
                stock_idx.append(board[y - i][x + i])
                if len(stock_idx) >= 3:
                    if stock_idx.count(player) == len(stock_idx):
                        a, b = y - i, x + i
                        print(player, "succeeds with a negative diagonal")
                        place_big_board(main_board, b // 3, a // 3, player)
                        stock_idx.clear()
                    else:
                        stock_idx.clear()


def check_empty_cells(board):
    if len(empty_cells_small_boards(board)) == 0:
        winner(0)


def check_big_board(main_board, player):
    for row in main_board:
        row_stock = []
        for i in range(len(main_board)):
            row_stock.append(row[i])
        if row_stock.count(player) == len(row_stock):
            #print(player, "Wins the match")
            winner(player)
            return True

    for col in range(len(main_board)):
        col_stock = []
        for row in main_board:
            col_stock.append(row[col])
        if col_stock.count(player) == len(col_stock) and col_stock[0] != 0:
            #print(player, "Wins the match")
            winner(player)
            return True

    diag_1 = []
    for idx in range(len(main_board)):
        diag_1.append(main_board[idx][idx])
    if len(diag_1) == diag_1.count(player):
        #print(player, "Wins the Match")
        winner(player)
        return True

    diag_2 = []
    for idx, rev_idx in enumerate(reversed(range(len(main_board)))):
        diag_2.append(main_board[idx][rev_idx])
    if diag_2.count(player) == len(diag_2):
        #print(player, "Wins the Match")
        winner(player)
        return True

    if len(empty_cells_big_board(main_board)) == 0:
        #print("No One Wins")
        winner(0)
        return True


def check_game(board, main_board, player):
    # Check horizontally
    check_horizontally(board, main_board, player)

    # Check vertically
    check_vertically(board, main_board, player)

    # Check diagonals
    check_diagonals(board, main_board, player)

    # Check empty cells
    check_empty_cells(board)
