
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
        stroke(random(255), random(255), random(255))
        
        x_margin = float(board_width) * (float(margin_percent) / 100)
        y_margin = float(board_height) * (float(margin_percent) / 100)

        # draw horizontal lines
        horizontal_line_spacing = (board_height - (2*y_margin)) / (self.rows)
        for i in range(1, self.rows):
            x_start = x_offset + x_margin
            x_end = x_offset + board_width - x_margin
            y = y_offset + y_margin + (i * horizontal_line_spacing)
            line(x_start, y, x_end, y)
        
        # draw vertical lines
        vertical_line_spacing = (board_width - (2*x_margin)) / (self.cols)
        for i in range(1, self.cols):
            x = x_offset + x_margin + (i * vertical_line_spacing)
            y_start = y_offset + y_margin
            y_end = y_offset + board_height - y_margin
            line(x, y_start, x, y_end)

        print("\n\n")
        
        # base case
        if self.depth == 0:
            textAlign(CENTER, CENTER)
            textSize(horizontal_line_spacing)
            for i, row in enumerate(self.spaces):
                for j, space in enumerate(row):
                    x = x_offset + x_margin + (j * vertical_line_spacing) + (vertical_line_spacing / 2)
                    y = y_offset + y_margin + (i * horizontal_line_spacing) + (horizontal_line_spacing / 2)
                    fill(0)
                    text(space, x, y)
        
        else:
            for i, row in enumerate(self.spaces):
                for j, space in enumerate(row):
                    next_x_offset = x_offset + x_margin + (j * vertical_line_spacing)
                    next_y_offset = y_offset + y_margin + (i * horizontal_line_spacing)
                    next_board_width = vertical_line_spacing
                    next_board_height = horizontal_line_spacing
                    space.display(next_x_offset, next_y_offset, next_board_height, next_board_width, margin_percent)
