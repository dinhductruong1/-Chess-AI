import asyncio
import chess
import chess.engine


board = chess.Board()

board.set_fen("rn1qkbnr/pPpb1ppp/4p3/8/3p4/8/PP1PPPPP/RNBQKBNR w KQkq - 1 5") #Position to try to promote "b7a8"
print(board)

while True:
    mover = input("Make your move: ")
    prueba = None
    try:
        prueba = chess.Move.from_uci(mover)
    except ValueError:
        pass
    if prueba not in board.legal_moves:
        try:
            if chess.Move.from_uci(mover + "q") in board.legal_moves:
                mover += input("Which piece you want to promote the pawn to? [q,r,b,n]: ")
                prueba = chess.Move.from_uci(mover)
                print
                print(board)
        except ValueError:
            pass
    if prueba in board.legal_moves:
        break
    print ("that is not a good move, make another valid move")