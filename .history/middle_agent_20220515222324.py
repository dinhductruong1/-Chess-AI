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