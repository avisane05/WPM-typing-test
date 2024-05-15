import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed typing test!")
    stdscr.addstr("Press any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    targat_text = "Hello world this is some text for this app!"
    current_text = []
    
    stdscr.clear()
    stdscr.addstr(targat_text)
    stdscr.refresh()




def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)