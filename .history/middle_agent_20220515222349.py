import chess

class MinimaxPlayer:
    def __init__(self, player) -> None:
        self.player = player

    def evalute_board_withscore(self, board):
        player = self.player
        player_score = \
            len(board.pieces(chess.PAWN, player))*100 +\
            len(board.pieces(chess.KNIGHT, player))*320 +\
            len(board.pieces(chess.BISHOP, player))*330 +\
            len(board.pieces(chess.ROOK, player))*500 +\
            len(board.pieces(chess.QUEEN, player))*900 +\
            len(board.pieces(chess.KING, player))*20000

        opponent_score = \
            len(board.pieces(chess.PAWN, not player))*100 +\
            len(board.pieces(chess.KNIGHT, not player))*320 +\
            len(board.pieces(chess.BISHOP, not player))*330 +\
            len(board.pieces(chess.ROOK, not player))*500 +\
            len(board.pieces(chess.QUEEN, not player))*900 +\
            len(board.pieces(chess.KING, not player))*20000

        return player_score - opponent_score

    def minimax(self, board, depth, alpha, beta, player):
        if depth == 0:
            return board_evaluation(board)

        if player:
            best = -100000
            for move in list(board.legal_moves):
                board.push(move)
                best = max(best, self.minimax(
                    board, depth-1, alpha, beta, not player))
                board.pop()

                alpha = max(alpha, best)
                if alpha >= beta:
                    return best
            return best
        else:
            best = 100000
            for move in list(board.legal_moves):
                board.push(move)
                best = min(best, self.minimax(
                    board, depth-1, alpha, beta, not player))
                board.pop()

                beta = min(beta, best)
                if alpha >= beta:
                    return best
            return best

    def get_move(self, board, depth):
        best = -100000
        best_move = None
        for move in list(board.legal_moves):
            board.push(move)
            move_value = self.minimax(board, depth, -100000, 100000, self.player)
            if move_value > best:
                best = move_value
                best_move = move
            board.pop()
        return best_move