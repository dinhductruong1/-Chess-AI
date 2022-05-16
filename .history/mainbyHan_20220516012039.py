import menugame
import chess
from draw_board import *
import minimax_agent
import random_agent
import middle_agent
from tkinter import messagebox
from time import sleep
DEPTH = 3
minimax_chess_color = True
human_chess_color = False
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
draw_board(screen)
load_image()
board = chess.Board()
bot1 = random_agent.RandomPlayer(not human_chess_color)
bot2 = random_agent.RandomPlayer(False)

selected_icon = pygame.transform.scale(
    pygame.image.load("images/selected.png"), (SQ_SIZE, SQ_SIZE))
bot_1 = minimax_agent.MinimaxPlayer(human_chess_color)


def game_over(key):
    if key == '1':
        if messagebox.askretrycancel("Gameover", "Bên trắng đã thắng"):
            menugame.cont()
    elif key == '0':
        if messagebox.askretrycancel("Gameover", "Bên đen đã thắng"):
            menugame.cont()
    else:
        if messagebox.askretrycancel("Gameover", "Hòa"):
            menugame.cont()
    pygame.quit()
    quit()


def human_vs_bot(human_chess_color):
    first_click = False
    second_click = False
    r1 = c1 = r2 = c2 = 0
    first_square = None
    second_square = None

    src_square = dest_square = -1

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
                        second_click = True

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
                                    last_move = move

            if first_square in list(set(move.from_square for move in list(board.legal_moves))):
                screen.blit(selected_icon, (c1 * SQ_SIZE, r1 * SQ_SIZE))
                target_squares = list(set(move.to_square for move in list(
                    board.legal_moves) if move.from_square == first_square))
                for x in target_squares:
                    screen.blit(selected_icon, ((x % 8) *
                                SQ_SIZE, (7-(x//8)) * SQ_SIZE))
        else:
            if isinstance(bot_1, random_agent.RandomPlayer):
                move = bot_1.get_move(board)
            else:
                move = bot_1.get_move(board, DEPTH)
            board.push(move)
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

        pygame.display.flip()


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
                    move = bot1.get_move(board, 3)
                board.push(move)
            else:
                if isinstance(bot2, random_agent.RandomPlayer):
                    move = bot2.get_move(board)
                move = bot2.get_move(board)
                board.push(move)
        else:
            draw_piece(screen, convert_to_int(board))
            pygame.display.flip()
            game_over(board.result()[0])

        pygame.display.flip()
        sleep(0.5)


def get_level(option, turn):
    options = {0: random_agent.RandomPlayer(), 1: middle_agent.MiddlePlayer(
        turn), 2: minimax_agent.MinimaxPlayer(turn)}
    return options[option]


def start_game(option):
    pass


bot_vs_bot()
