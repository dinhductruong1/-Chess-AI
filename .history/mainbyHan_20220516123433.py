from typing import Tuple, Any
import pygame_menu.widgets
from pygame_menu.examples import create_example_window
import pygame_menu
import chess
from draw_board import *
import minimax_agent
import random_agent
import middle_agent
from tkinter import messagebox
from time import sleep


def get_level(option=0, turn=False):
    options = {0: random_agent.RandomPlayer(turn), 1: middle_agent.MiddleAgent(
        turn), 2: minimax_agent.MinimaxPlayer(turn)}
    return options[option]


DEPTH = 3
human_chess_color = False
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
draw_board(screen)
load_image()
board = chess.Board()
bot1 = get_level()
bot2 = get_level()

selected_icon = pygame.transform.scale(
    pygame.image.load("images/selected.png"), (SQ_SIZE, SQ_SIZE))


def game_over(key):
    if key == '1':
        if messagebox.askretrycancel("Gameover", "Bên trắng đã thắng"):
            cont()
    elif key == '0':
        if messagebox.askretrycancel("Gameover", "Bên đen đã thắng"):
            cont()
    else:
        if messagebox.askretrycancel("Gameover", "Hòa"):
            cont()
    pygame.quit()
    quit()


def human_vs_bot():
    first_click = False
    r1 = c1 = r2 = c2 = 0
    first_square = None
    second_square = None
    src_square = dest_square = -1
    global bot1
    while 1:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                if messagebox.askokcancel("Thông báo", "Bạn có muốn thoát không?"):
                    pygame.quit()
                    quit()

        draw_piece(screen, convert_to_int(board))
        last_move = None
        if board.turn == human_chess_color:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        if board.move_stack:
                            board.pop()
                            board.pop()
                            last_move = None
                            src_square = dest_square = -1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not first_click:
                        c1 = int(pygame.mouse.get_pos()[0]/SQ_SIZE)
                        r1 = int(pygame.mouse.get_pos()[1]/SQ_SIZE)
                        first_square = (7-r1)*8+c1
                        first_click = True

                    if first_click:
                        c2 = int(pygame.mouse.get_pos()[0]/SQ_SIZE)
                        r2 = int(pygame.mouse.get_pos()[1]/SQ_SIZE)
                        second_square = (7-r2)*8+c2

                        target_squares = list(set(move.to_square for move in list(
                            board.legal_moves) if move.from_square == first_square))

                        if second_square not in target_squares:
                            c1 = c2
                            r1 = r2
                            first_square = (7-r1)*8+c1
                        else:
                            for move in list(board.legal_moves):
                                if move.from_square == first_square and move.to_square == second_square:
                                    board.push(move)
                                    draw_piece(screen, convert_to_int(board))
                                    pygame.display.flip()
                                    last_move = move

            if first_square in list(set(move.from_square for move in list(board.legal_moves))):
                screen.blit(selected_icon, (c1 * SQ_SIZE, r1 * SQ_SIZE))
                target_squares = list(set(move.to_square for move in list(
                    board.legal_moves) if move.from_square == first_square))
                for x in target_squares:
                    screen.blit(selected_icon, ((x % 8) *
                                SQ_SIZE, (7-(x//8)) * SQ_SIZE))
        else:
            if isinstance(bot1, random_agent.RandomPlayer):
                move = bot1.get_move(board)
            else:
                move = bot1.get_move(board, DEPTH)
            board.push(move)
            draw_piece(screen, convert_to_int(board))
            pygame.display.flip()
            last_move = move

        if last_move:
            src_square = last_move.from_square
            dest_square = last_move.to_square

        screen.blit(selected_icon, ((src_square % 8) *
                    SQ_SIZE, (7-(src_square//8)) * SQ_SIZE))
        screen.blit(selected_icon, ((dest_square % 8) *
                    SQ_SIZE, (7-(dest_square//8)) * SQ_SIZE))

        if board.is_game_over():
            draw_piece(screen, convert_to_int(board))
            pygame.display.flip()
            game_over(board.result()[0])


def bot_vs_bot():

    while 1:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                if messagebox.askokcancel("Thông báo", "Bạn có muốn thoát không?"):
                    pygame.quit()
                    quit()
        draw_piece(screen, convert_to_int(board))
        if not board.is_game_over():
            if board.turn == bot1.player:
                if isinstance(bot1, random_agent.RandomPlayer):
                    move = bot1.get_move(board)
                else:
                    move = bot1.get_move(board, DEPTH)
                board.push(move)
            else:
                if isinstance(bot2, random_agent.RandomPlayer):
                    move = bot2.get_move(board)
                else:
                    move = bot2.get_move(board, DEPTH)
                board.push(move)
        else:
            draw_piece(screen, convert_to_int(board))
            pygame.display.flip()
            game_over(board.result()[0])

        pygame.display.flip()
        sleep(0.5)


surface = create_example_window('Cờ vua', (512, 512))
is_human = True


def set_mode(selected: Tuple, value=0) -> None:
    global is_human
    is_human = False if value == 1 else True
    print('is_human:', is_human)


def set_chess_color(selected: Tuple, value: Any):
    global human_chess_color
    if value == 0:
        human_chess_color = True
    else:
        human_chess_color = False


def set_bot1(selected: Tuple, value: Any):
    global bot1
    bot1 = get_level(value)


def set_bot2(selected: Tuple, value: Any):
    global bot2
    bot2 = get_level(value)


def start_the_game():
    global bot1, bot2
    if is_human:
        bot1.player = not human_chess_color
        human_vs_bot()
    else:
        bot1.player = chess.WHITE
        bot2.player = chess.BLACK
        bot_vs_bot()


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Nhập môn trí tuệ nhân tạo',
    width=512
)

menu.add.dropselect(
    title='Chọn chế độ',
    items=[('Đánh với máy ', 0),
           ('Máy với máy', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_mode
)
menu.add.dropselect(
    title='Chọn màu cờ',
    items=[('Trắng: đi trước', 0),
           ('Đen: đi sau', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_chess_color
)
menu.add.dropselect(
    title='Độ khó BOT 1',
    items=[('Dễ', 0),
           ('Trung bình', 1),
           ('Khó', 2), ],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_bot1
)
menu.add.dropselect(
    title='Độ khó BOT 2',
    items=[('Dễ', 0),
           ('Trung bình', 1),
           ('Khó', 2), ],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_bot2
)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


def cont():
    board.reset()
    menu.mainloop(surface)


cont()
