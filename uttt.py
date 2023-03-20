import time

import pygame
import os
import random

from board import NewBoard

from frontend import fill
from frontend import update_window

from check_game import check_big_board
from check_game import get_possible_moves
from check_game import validate_box
from check_game import set_locations
from check_game import check_game

from minimax import minimax
from minimax2 import minimax2
from alpha_beta import minimax_alpha_beta

#depth
depth = 6

# variable initialization for frontend
pygame.font.init()
width, height = 810, 810
final_square = 750
square = width // 3
small_square = square // 3
margin = width // 30

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ultimate Tic Tac Toe")
clock = pygame.time.Clock()

# asset initialization
free_square = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "FreeSpaces.png")), (small_square, small_square))

small_cross = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "cross.png")), (small_square, small_square))
cross = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "cross.png")), (square, square))
final_cross = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "cross.png")), (final_square, final_square))

small_circle = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "circle.png")), (small_square, small_square))
circle = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "circle.png")), (square, square))
final_circle = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "circle.png")), (final_square, final_square))
final_draw = pygame.transform.scale(pygame.image.load(os.path.join(
    "Assets",
    "Draw.png")), (final_square, final_square))

# graphic color setting
bg = (250, 250, 250)
lines_color_1 = (0, 0, 0)
lines_color_2 = (0, 200, 0)

# creates logical board, which has function to construct arrays for global (3x3) and local boards (9x9)
game_board = NewBoard()


def main():
    run = True
    turn = -1#random.choice([-1, 1])
    ai = 1
    human = -1
    fps = 60
    red = (178, 0, 0, 0)
    green = (0, 178, 0, 0)
    blue = (0, 0, 178, 0)
    game_over = False
    box = None
    turn_time = []
    main_board = game_board.create_board()
    small_boards = game_board.every_small_boards()

    clock.tick(fps)
    fill(small_circle, green)
    fill(circle, green)
    fill(final_circle, green)

    fill(small_cross, blue)
    fill(cross, blue)
    fill(final_cross, blue)

    fill(final_draw, red)

    # draws the GUI representation of a board
    update_window(win, lines_color_1, lines_color_2, width, free_square, final_square, square,
                  small_square,
                  margin, small_cross, small_circle, cross, circle, final_circle, final_cross, final_draw, small_boards,
                  main_board, bg, box)

    while run:
        update_window(win, lines_color_1, lines_color_2, width, free_square, final_square, square,
                      small_square,
                      margin, small_cross, small_circle, cross, circle, final_circle, final_cross, final_draw,
                      small_boards,
                      main_board, bg, box)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            # on pressing keydown resets the game after game over
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    game_board.reset(small_boards, main_board, game_over)
                    game_over = False

            # main program for human player, which checks on mouse click position, validates the turn and sets the cell
            # with cross/circle. On the logical board, player turn is represented as -1 and AI as 1
            if event.type == pygame.MOUSEBUTTONDOWN and turn == human and not game_over:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    if set_locations(small_boards, main_board, pos[0] // small_square, pos[1] // small_square,  turn, box):
                        check_game(small_boards, main_board, turn)
                        new_box = get_possible_moves(small_boards,
                                                     pos[0] // small_square,
                                                     pos[1] // small_square)
                        box = validate_box(small_boards, main_board, new_box,
                                           pos[0] // small_square,
                                           pos[1] // small_square)
                        update_window(win, lines_color_1, lines_color_2, width, free_square, final_square, square,
                                      small_square,
                                      margin, small_cross, small_circle, cross, circle, final_circle, final_cross,
                                      final_draw, small_boards,
                                      main_board, bg, box)
                        if check_big_board(main_board, turn):
                            game_over = True
                        turn = ai
        if turn == ai:

            start = time.time()
            #new_board, value, pos = minimax(small_boards, main_board, depth, box, turn, True)
            #new_board, value, pos = minimax2(small_boards, main_board, depth, box, turn, True)
            new_board, value, pos = minimax_alpha_beta(small_boards, main_board, depth, box, turn, True)
            end = time.time() - start
            print(f"AI's turn time: {end}")
            turn_time.append(end)
            small_boards = new_board
            check_game(small_boards, main_board, turn)

            new_box = get_possible_moves(small_boards, pos[0], pos[1])
            box = validate_box(small_boards, main_board, new_box, pos[0],
                               pos[1])

            if check_big_board(main_board, turn):
                game_over = True
            turn = human




main()
