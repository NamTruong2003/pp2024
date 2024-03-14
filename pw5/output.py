import input as ip
import curses
def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.refresh()
    for _ in range(ip.numberCourse*ip.numberStudent):
        stdscr.addstr(_,0,f"course: {ip.listMark[_].course} id: {ip.listMark[_].id} name: {ip.listMark[_].name} mark: {ip.listMark[_].mark}")
    stdscr.refresh()
    stdscr.getch()