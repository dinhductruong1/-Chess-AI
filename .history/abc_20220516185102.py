import asyncio
import chess
import chess.engine


board = chess.Board()

board.set_fen("rn1qkbnr/pPpb1ppp/4p3/8/3p4/8/PP1PPPPP/RNBQKBNR w KQkq - 1 5") #Position to try to promote "b7a8"

In case the move is invalid, you could check whether adding "q" to it makes it valid. If so, then it must be that this is a pawn promotion move and you could then ask the user which piece they want to promote the pawn to.

So:

if prueba in board.legal_moves:
    if board.is_castling(prueba):
        print("good job castling!")
else:
    if chess.Move.from_uci(mover + "q") in board.legal_moves:
        mover += input("Which piece you want to promote the pawn to? [q,r,b,n]: ")
        prueba = chess.Move.from_uci(mover)
    if prueba not in board.legal_moves:
        print ("that is not a good move, make another valid")
        mover = input("a valid move please: ")
Still, there are some issues you would like to deal with:

There can be an exception when the input does not even resemble a move
Even after the above code, you may be left with an invalid move, so there really should be a loop that continues until the move is valid:
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
        except ValueError:
            pass
    if prueba in board.legal_moves:
        break
    print ("that is not a good move, make another valid move")