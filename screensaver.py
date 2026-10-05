import curses

from custom_addstr import (
    bottom_center_addstr,
    bottom_left_addstr,
    bottom_right_addstr,
    centered_addstr,
    top_center_addstr,
    top_left_addstr,
    top_right_addstr,
)

DEFAULT_ROW_GAP = 4

def parse_sprite(sprite: str) -> list:
    array_output = []
    for linea in sprite.split('\n'):
        cleansed = linea
        array_output.append(cleansed)
    return array_output

def parse_text(text: str) -> list:
    array_output = []
    for linea in text.split('\n'):
        cleansed = linea#.strip()
        array_output.append(cleansed)
    return array_output

def get_row_height(sprite_l, sprite_c, sprite_r) -> int:
    height_l = len(sprite_l) 
    height_c = len(sprite_c)
    height_r = len(sprite_r)
    return max(height_l, height_c, height_r) + DEFAULT_ROW_GAP

def get_text_height(text_array) -> int:
    return len(text_array) + 1

def main_loop(
        stdscr,
        centered_text: str,
        top_left: str       = "",
        top_center: str     = "",
        top_right: str      = "",
        bottom_left: str    = "",
        bottom_center: str  = "",
        bottom_right: str   = "",
        title: str          = ""
    ):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(False)
    stdscr.addstr(0,0, title)

    # loads message
    message = parse_text(centered_text)
    # loads sprites to be prnted
    top_left_print = parse_sprite(top_left)
    top_center_print = parse_sprite(top_center)
    top_right_print = parse_sprite(top_right)
    bottom_left_print = parse_sprite(bottom_left)
    bottom_center_print = parse_sprite(bottom_center)
    bottom_right_print = parse_sprite(bottom_right) 

    # gets dimensions of initial layout
    height, width = stdscr.getmaxyx()
    top_row_height = get_row_height(bottom_left_print, bottom_center_print, bottom_right_print)
    bottom_row_height = get_row_height(top_left_print, top_center_print, top_right_print)
    message_height = get_text_height(message)
    sprites_height = top_row_height + message_height + bottom_row_height

    while True:
        stdscr.erase()

        # prints sprites
        try:
            if (sprites_height) <= height:
                # prints top row
                top_left_addstr(stdscr, width, height, top_left_print)
                top_center_addstr(stdscr, width, height, top_center_print)
                top_right_addstr(stdscr, width, height, top_right_print)
                # prints centered text.
                centered_addstr(stdscr, width, height, message)
                # prints bottom row
                bottom_left_addstr(stdscr, width, height, bottom_left_print)
                bottom_center_addstr(stdscr, width, height, bottom_center_print)
                bottom_right_addstr(stdscr, width, height, bottom_right_print)
            
            elif (sprites_height - top_row_height) < height:
                centered_addstr(stdscr, width, top_row_height, message)
                # prints bottom row
                bottom_left_addstr(stdscr, width, height, bottom_left_print)
                bottom_right_addstr(stdscr, width, height, bottom_center_print) # sets center ascii on right

            else:                
                centered_addstr(stdscr, width, height, bottom_center_print)

        except curses.error:
            pass

        stdscr.refresh()
        c = stdscr.getch()

        # prevents exit on resizing
        if c == curses.KEY_RESIZE:
            height, width = stdscr.getmaxyx()
            # gets dimensions of new resized layout
            top_row_height = get_row_height(bottom_left_print, bottom_center_print, bottom_right_print)
            bottom_row_height = get_row_height(top_left_print, top_center_print, top_right_print)
            message_height = get_text_height(message)
            sprites_height = top_row_height + message_height + bottom_row_height
            stdscr.erase()
            stdscr.refresh()
        else:
            break

    