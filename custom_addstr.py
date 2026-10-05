
COLUMN_DIVISION = 10

def safe_addstr(stdscr, y, x, text, attr=0):
    #
    #    pasted from stack overflow
    #   
    max_y, max_x = stdscr.getmaxyx()  
    
    # Check if starting point is inside the screen bounds
    if not (0 <= y < max_y) or not (0 <= x < max_x):
        return False  # Out of bounds     
    # Check if the string extends past the right edge
    if x + len(text) > max_x:
        return False  # Too long for the line  
    
    # Prevent hitting the exact bottom-right error corner if necessary
    if y == max_y - 1 and x + len(text) >= max_x:
        return False  # Would write into lower-right corner exception zone      

    stdscr.addstr(y, x, text, attr)
    return True


def centered_addstr(stdscr, width, height, array_print: list, attr=0):
    sprite_w = min([len(w) for w in array_print])
    center_x = (width - sprite_w) // 2
    center_y = (height - len(array_print)) // 2 
    
    for i in range(len(array_print)-1):
        line = array_print[i]
        inner_padding = sprite_w - len(line) // 2
        safe_addstr(stdscr, center_y + i, center_x + inner_padding, line)
        
def bottom_left_addstr(stdscr, width, height, array_print: list, attr=0):
    # vertical lenght
    vertical_l = len(array_print) + 1 
    bottom_x = (width) // COLUMN_DIVISION
    bottom_y = (height) - vertical_l
    
    for i in range(len(array_print)-1):
        line = array_print[i]
        safe_addstr(stdscr, bottom_y + i, bottom_x, line)
        
def bottom_right_addstr(stdscr, width, height, array_print: list, attr=0):
    # horizontal width
    sprite_w = max([len(w) for w in array_print])
    # vertical lenght
    vertical_l = len(array_print) + 1 
    horizontal_padding = COLUMN_DIVISION - 1
    bottom_x = ((width) // COLUMN_DIVISION ) * horizontal_padding - sprite_w
    bottom_y = (height)
    
    for i in range(len(array_print)-1):
        line = array_print[i]
        safe_addstr(stdscr, bottom_y - vertical_l + i, bottom_x, line)

def bottom_center_addstr(stdscr, width, height, array_print: list, attr=0):
    sprite_w = max([len(w) for w in array_print])
    center_x =  (width - sprite_w) // 2
    bottom_y = (height - len(array_print)) 
    
    for i in range(len(array_print)-1):
        line = array_print[i]
        safe_addstr(stdscr, bottom_y + i, center_x, line)
        
def top_left_addstr(stdscr, width, height, array_print: list, attr=0):
    bottom_x = (width) // COLUMN_DIVISION
    bottom_y = (height) // COLUMN_DIVISION
    
    for i in range(len(array_print)-1):
        line = array_print[i]
        safe_addstr(stdscr, bottom_y + i, bottom_x, line)

def top_center_addstr(stdscr, width, height, array_print: list, attr=0):
    sprite_w = max([len(w) for w in array_print])
    center_x =  (width - sprite_w) // 2
    top_y = (height) // COLUMN_DIVISION 
        
    for i in range(len(array_print)-1):
        line = array_print[i]
        safe_addstr(stdscr, top_y + i, center_x, line)

def top_right_addstr(stdscr, width, height, array_print: list, attr=0):
    # horizontal width
    sprite_w = max([len(w) for w in array_print])
    # vertical lenght
    vertical_l = len(array_print) + 1 
    horizontal_padding = COLUMN_DIVISION - 1
    top_x = ((width) // COLUMN_DIVISION ) * horizontal_padding - sprite_w
    top_y = ((height) // COLUMN_DIVISION) + vertical_l
    
    for i in range(len(array_print)-1):
        line = array_print[i]
        safe_addstr(stdscr, top_y - vertical_l + i, top_x, line)
