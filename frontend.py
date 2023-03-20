import pygame


last_turn_id = None
winnerId = None


def fill(surface, color):
    # fills a surface with color, used to recolor color cross/circle assets
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def draw_pieces(win, free_square, small_cross, small_circle, small_square, board, box):
    if box:
        for q in range(len(box)):
            win.blit(free_square, (box[q][0] * small_square, box[q][1] * small_square))

    for x1 in range(len(board)):
        for y1 in range(len(board)):
            if board[y1][x1] == -1:
                #print(f'small circle: {y1} * {x1}')
                win.blit(small_circle, (x1 * small_square, y1 * small_square))

            if board[y1][x1] == 1:
                #print(f'small cross: {y1} * {x1}')
                win.blit(small_cross, (x1 * small_square, y1 * small_square))



def draw_big_pieces(win, big_board, square, circle, cross):
    for x2 in range(len(big_board)):
        for y2 in range(len(big_board)):
            if big_board[y2][x2] == -1:
                #print(f'small piece: {y2} * {x2}')
                win.blit(circle, (x2 * square, y2 * square))

            if big_board[y2][x2] == 1:
                #print(f'small piece: {y2} * {x2}')
                win.blit(cross, (x2 * square, y2 * square))


def draw_board(win, lines_color_1, lines_color_2, width, square, small_square,
               margin):
    height = width

    # Small Boards
    for move in range(0, 3):
        for ab in range(0, 3):
            for x in range(1, 3):  # Vertical lines
                pygame.draw.line(win, lines_color_2, (
                    margin + square * move, (x * small_square) + ab * square), (
                                     (square - margin) + square * move,
                                     (x * small_square) + ab * square), 1)

            for bc in range(0, 2):
                for y in range(3):  # Horizontal lines
                    pygame.draw.line(win, lines_color_2, (
                        small_square + bc * small_square + move * square,
                        margin + ab * square), (
                                         small_square + bc * small_square + move * square,
                                         (square - margin) + ab * square), 1)

    # Big Board
    for i in range(1, 3):  # Draw horizontal lines
        pygame.draw.line(win, lines_color_1, (0, square * i), (width, square * i),
                         2)

    for j in range(1, 3):  # Draw vertical lines
        pygame.draw.line(win, lines_color_1, (square * j, 0),
                         (square * j, height), 2)


def winner(player):
    if player == -1:
        msg = "Human wins"
        print(msg)
        winnerId = -1

    elif player == 1:
        msg = "Computer wins"
        print(msg)
        winnerId = 1

    else:
        msg = "No one wins"
        print(msg)
        winnerId = 2


def update_window(win, lines_color_1, lines_color_2, width, free_square, final_square, square,
                  small_square,
                  margin, small_cross, small_circle, cross, circle, final_circle, final_cross, final_draw, board,
                  big_board, bg, box):
    #print("update window started")
    win.fill(bg)

    # draws small pieces
    draw_pieces(win, free_square, small_cross, small_circle, small_square, board, box)

    # draws the board itself
    draw_board(win, lines_color_1, lines_color_2, width, square, small_square,
               margin)

    # draws big pieces
    draw_big_pieces(win, big_board, square, circle, cross)
    draw_final(win, final_cross, final_circle, final_draw, final_square)
    pygame.display.update()
    #print("update window finished\n\n")




def highlight(win, big_board, square, circle, cross):
    for x2 in range(len(big_board)):
        for y2 in range(len(big_board)):
            if big_board[y2][x2] == -1:
                win.blit(circle, (x2 * square, y2 * square))

            if big_board[y2][x2] == 1:
                win.blit(cross, (x2 * square, y2 * square))


def draw_final(win, final_cross, final_circle, final_draw, final_square):
    match winnerId:
        case -1:
            #print("hjhjh")
            win.blit(final_circle, final_square, final_square)
        case  1:
            win.blit(final_cross, final_square, final_square)
        case  0:
            win.blit(final_draw, final_square, final_square)
        case _:
            #print("still there is no winner")
            if False:
                print("still there is no winner")

