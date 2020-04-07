
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

    def display(self, x_offset, y_offset, board_height, board_width, margin_percent):
        
        # draw horizontal lines
        margin = board_height * (margin_percent / 100)
        horizontal_line_spacing = (board_height - (2*margin)) / (self.rows)
        for i in range(1, self.rows - 1):
            line(x_offset + margin, y_offset + (i * horizontal_line_spacing), x_offset + (board_width - margin), y_offset + (i * horizontal_line_spacing))
        
        # draw vertical lines
        margin = board_width * margin_percent
        vertical_line_spacing = (board_width - (2*margin)) / (self.cols)
        for i in range(1, self.cols - 1):
            line(x_offset + (i*vertical_line_spacing), y_offset + margin, x_offset + (i*vertical_line_spacing), y_offset + (board_height-margin))
        
        # base case
        if self.depth == 0:
            textAlign(CENTER, CENTER)
            textSize(board_height/self.rows)
            for i, row in enumerate(self.spaces):
                for j, space in enumerate(row):
                    x = x_offset + (j * vertical_line_spacing) + (vertical_line_spacing / 2)
                    y = y_offset + (i * horizontal_line_spacing) + (horizontal_line_spacing / 2)
                    text(space, x, y)
        
        else:
            for i, row in enumerate(self.spaces):
                for j, space in enumerate(row):
                    next_x_offset = x_offset + (board_width / self.cols)
                    next_y_offset = y_offset + (board_height / self.rows)
                    next_board_width = board_width / self.cols
                    next_board_height = board_height / self.rows
                    space.display(next_x_offset, next_y_offset, next_board_height, next_board_width, margin_percent)
