from draw_board import *

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION

class HumanPlayer:
    def __init__(self) -> None:
        self.selected = pygame.transform.scale(pygame.image.load("images/selected.png"), (SQ_SIZE, SQ_SIZE))
        pass

    def get_move(self, screen, board):
        
        first_click = False
        second_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                c1 = int(pygame.mouse.get_pos()[0]/SQ_SIZE)
                r1 = int(pygame.mouse.get_pos()[1]/SQ_SIZE)
                selected_square = (7-r1)*8+c1
                if selected_square in list(set(move.from_square for move in list(board.legal_moves))):
                    first_click = True
                    screen.blit(self.selected, (c1 * SQ_SIZE, r1 * SQ_SIZE))
                    target_squares = list(set(move.to_square for move in list(board.legal_moves) if move.from_square == selected_square))
                    for x in target_squares:
                        screen.blit(self.selected, ((x%8) * SQ_SIZE, (7-(x//8)) * SQ_SIZE))
        drawpiece(screen, convert_to_int(board))
        pygame.display.flip()
