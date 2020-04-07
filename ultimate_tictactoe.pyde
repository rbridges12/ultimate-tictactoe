from Board import Board

def make_board(board):
    if board.get_depth() == 0:
        board.make_base_board()
    
    else:
        for i in range(board.get_rows()):
            for j in range(board.get_cols()):
                 board.set_space(i, j, Board(depth = board.get_depth() - 1))
                 make_board(board.get_space(i, j))
                 
def fill_board(board, content):
    try:
        for row in board.get_spaces():
            for space in row:
                fill_board(space, content)
    except:
        for i, row in enumerate(board.get_spaces()):
            for j, space in enumerate(row):
                board.set_space(i, j, content)
        
def setup():
    size(600, 600)
    background(255)
    strokeWeight(4)
    board = Board(depth = 1)
    make_board(board)
    
    #print(board)
    
    fill_board(board, "X")
    board.display(0, 0, height, width, 10)
