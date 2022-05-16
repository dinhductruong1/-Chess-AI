import asyncio
import chess
import chess.engine


board = chess.Board()

board.set_fen("rn1qkbnr/pPpb1ppp/4p3/8/3p4/8/PP1PPPPP/RNBQKBNR w KQkq - 1 5") #Position to try to promote "b7a8"

while not board.is_game_over():
   
    print(board)

    mover = input("Make your move")
    

    prueba = chess.Move.from_uci(mover)
    
    
    if prueba in board.legal_moves:
        if board.is_castling(prueba):
            print("good you castling")
    else:
        print ("that is not a good move, make another valid")
        mover = input("a valid move please: ")

    if prueba.promotion != None:
        print ("This is a promotion (or was)")
        
    board.push_xboard(mover)
        
    print(board)
    
    board.push(result.move)
    
    print(board)