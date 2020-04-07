from Board import Board

def make_board(board):
    if board.get_depth() == 0:
        board.make_base_board()
    
    else:
        for i in range(board.get_rows()):
            for j in range(board.get_cols()):
                 board.set_space(i, j, Board(depth = board.get_depth() - 1))
                 make_board(board.get_space(i, j))
        
def setup():
    size(200, 200)
    background(255)
    fill(0)
    stroke(10)
    board = Board(depth = 2)
    make_board(board)
    #print(board)
    
    board.display(0, 0, height, width, 10)
