
class Board:
    
    def __init__(self, depth = 0, rows = 3, cols = 3):
        self.depth = depth
        self.rows = rows
        self.cols = cols
        self.spaces = [ ([None] * self.cols) for row in range(self.rows) ]
        
    def set_space(self, row, col, val):
        self.spaces[row][col] = val
        
    def get_space(self, row, col):
        return self.spaces[row][col]
    
    def get_spaces(self):
        return self.spaces
    
    def get_depth(self):
        return self.depth
    
    def set_depth(self):
        return self.depth
    
    def get_rows(self):
        return self.rows
    
    def get_cols(self):
        return self.cols

    def make_base_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.spaces[i][j] = ""
    
    def __str__(self):
        s = "["
        for row in self.spaces:
            s += "["
            for space in row:
                s += "%s, " % str(space)
            s += "]"
        s += "]"
        return s
    
