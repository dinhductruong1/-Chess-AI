
import pygame

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}

def load_image():
    pieces = ['wp', 'bp', 'wn', 'bn', 'wr',
              'br', 'wb', 'bb', 'wq', 'bq', 'wk', 'bk']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(
            "images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def draw_board(screen):
    color = [pygame.Color("white"), pygame.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            pygame.draw.rect(screen, color[(r + c) % 2],
                        (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_piece(screen, board):
    color = [pygame.Color("white"), pygame.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            pygame.draw.rect(screen, color[(r + c) % 2],
                        (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if piece != '--':
                screen.blit(IMAGES[piece], (c * SQ_SIZE, r * SQ_SIZE))

def convert_to_int(board):
    dict = {
        '♚': 'bk',
        '♛': 'bq',
        '♜': 'br',
        '♝': 'bb',
        '♞': 'bn',
        '♟': 'bp',
        '⭘': '--',
        '♙': 'wp',
        '♘': 'wn',
        '♗': 'wb',
        '♖': 'wr',
        '♕': 'wq',
        '♔': 'wk'
    }
    unicode = board.unicode()
    newboard = [
        [dict[c] for c in row.split()]
        for row in unicode.split('\n')
    ]
    return newboard