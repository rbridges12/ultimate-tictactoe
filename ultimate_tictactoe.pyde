from Board import Board

def make_board(board, final_depth):
    print(board.get_depth())
    if board.get_depth() == final_depth:
        print("base case")
        board.make_base_board()
    
    else:
        for i in range(board.get_rows()):
            for j in range(board.get_cols()):
                 board.set_space(i, j, Board(depth = board.get_depth() + 1))
                 make_board(board.get_space(i, j), final_depth)
        
board = Board(depth = 0)
make_board(board, 0)
print(board)
