import chess
from draw_board import *
import minimax_agent
import random_agent
from time import sleep

def minimax_vs_random(minimax_chess_color):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    board = chess.Board()

    player1 = minimax_agent.MinimaxPlayer(minimax_chess_color)
    player2 = random_agent.RandomPlayer()
    
    draw_board(screen)
    load_image()
    black_win = pygame.transform.scale(pygame.image.load("images/bK.png"), (256, 256))
    white_win = pygame.transform.scale(pygame.image.load("images/wK.png"), (256, 256))
    while 1:
        draw_piece(screen, convert_to_int(board))

        if not board.is_game_over():
            if board.turn == player1.player:
                move = player1.get_move(board, 3)
                board.push(move)
            else:
                move = player2.get_move(board)
                board.push(move)
        else:
            if board.result()[0] == '1':
                screen.blit(white_win, (128, 128))
            elif board.result()[0] == '0':
                screen.blit(black_win, (128, 128))
            else:
                screen.blit(white_win, (0, 128))
                screen.blit(black_win, (256, 128))

        pygame.display.flip()
        sleep(1) 

def human_vs_minimax(human_chess_color):

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    draw_board(screen)
    load_image()
    board = chess.Board()

    selected_icon = pygame.transform.scale(pygame.image.load("images/selected.png"), (SQ_SIZE, SQ_SIZE))
    black_win = pygame.transform.scale(pygame.image.load("images/bK.png"), (256, 256))
    white_win = pygame.transform.scale(pygame.image.load("images/wK.png"), (256, 256))

    mimimax_player = minimax_agent.MinimaxPlayer(not human_chess_color)

    first_click = False
    second_click = False
    r1=c1=r2=c2=0
    first_square = None
    second_square = None

    src_square = dest_square = -1

    while 1:
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

                        target_squares = list(set(move.to_square for move in list(board.legal_moves) if move.from_square == first_square))

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
                target_squares = list(set(move.to_square for move in list(board.legal_moves) if move.from_square == first_square))
                for x in target_squares:
                    screen.blit(selected_icon, ((x%8) * SQ_SIZE, (7-(x//8)) * SQ_SIZE))
        else:
            move = mimimax_player.get_move(board, 2)
            board.push(move)
            last_move = move

        if last_move:
            src_square = last_move.from_square
            dest_square = last_move.to_square
        
        screen.blit(selected_icon, ((src_square%8) * SQ_SIZE, (7-(src_square//8)) * SQ_SIZE))
        screen.blit(selected_icon, ((dest_square%8) * SQ_SIZE, (7-(dest_square//8)) * SQ_SIZE))

        if board.is_game_over():
            if board.result()[0] == '1':
                screen.blit(white_win, (128, 128))
            elif board.result()[0] == '0':
                screen.blit(black_win, (128, 128))
            else:
                screen.blit(white_win, (128, 256))
                screen.blit(black_win, (128+256, 256))

        pygame.display.flip()

# minimax_vs_random(True)    
# human_vs_minimax(True)