import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_test(stdscr, targat, current, wpm=0):
    stdscr.addstr(targat)

    for i, char in enumerate(current):
        correct_char = targat[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
            
        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr):
    targat_text = "Hello world this is some text for this app!"
    current_text = []

    while True:        
        stdscr.clear()
        
        display_test(stdscr, targat_text, current_text)

        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(targat_text):
            current_text.append(key)





def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)