class NewBoard:
    def __init__(self):
        self.board_x = 3
        self.board_y = 3

    def create_board(self):
        return [[0 for _ in range(self.board_x)] for _ in range(self.board_y)]

    def every_small_boards(self):
        return [[0 for y in range(9)] for z in range(9)]

    def reset(self, board, main_board, game_over):
        if game_over:
            for x, row in enumerate(board):
                for y in range(len(row)):
                    board[y][x] = 0

            for x, row in enumerate(main_board):
                for y in range(len(row)):
                    main_board[y][x] = 0
