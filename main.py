from time import sleep
from more_itertools import first
from draw_board import *
import minimax_agent
import random_agent

def minimax_vs_random():
    pygame.init()
    PLAYER = False
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    board = chess.Board()
    player1 = minimax_agent.MinimaxPlayer(PLAYER)
    player2 = minimax_agent.MinimaxPlayer(not PLAYER)
    drawboard(screen)
    loadImage()
    while 1:
        if not board.is_game_over():
            if board.turn == player1.player:
                move = player1.get_move(board, 2)
                board.push(move)
            else:
                move = player2.get_move(board, 2)
                board.push(move)
        else:
            print(board.result())
        drawpiece(screen, convert_to_int(board))
        pygame.display.flip()
        sleep(1) 

def human_vs_minimax():
    HUMAN_TURN = True
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    drawboard(screen)
    loadImage()
    board = chess.Board()
    selectedIcon = pygame.transform.scale(pygame.image.load("images/selected.png"), (SQ_SIZE, SQ_SIZE))

    mimimax_player = minimax_agent.MinimaxPlayer(not HUMAN_TURN)

    first_click = False
    second_click = False
    r1=c1=r2=c2=0
    first_square = None
    second_square = None

    src_square = dest_square = -1

    while 1:
        drawpiece(screen, convert_to_int(board))
        last_move = None
        if board.turn == HUMAN_TURN:
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
                                    sleep(0.5)
                                    
            if first_square in list(set(move.from_square for move in list(board.legal_moves))):
                screen.blit(selectedIcon, (c1 * SQ_SIZE, r1 * SQ_SIZE))
                target_squares = list(set(move.to_square for move in list(board.legal_moves) if move.from_square == first_square))
                for x in target_squares:
                    screen.blit(selectedIcon, ((x%8) * SQ_SIZE, (7-(x//8)) * SQ_SIZE))
        else:
            move = mimimax_player.get_move(board, 2)
            board.push(move)
            last_move = move

        if last_move:
            src_square = last_move.from_square
            dest_square = last_move.to_square
        
        screen.blit(selectedIcon, ((src_square%8) * SQ_SIZE, (7-(src_square//8)) * SQ_SIZE))
        screen.blit(selectedIcon, ((dest_square%8) * SQ_SIZE, (7-(dest_square//8)) * SQ_SIZE))

        pygame.display.flip()
        
human_vs_minimax()