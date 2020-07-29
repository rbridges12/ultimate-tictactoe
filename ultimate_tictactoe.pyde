from Board import Board
        
def setup():
    size(700, 700)
    background(255)
    strokeWeight(1)
    board = Board(depth = 4)
    board.fill_board()
    board.set_spaces("X")
    board.display(5, color(0, 0, 0))
    
def draw():
    x=1

def mouseClicked():
    x = mouseX
    y = mouseY
    for i in range(board.get_depth()):
        x=1
