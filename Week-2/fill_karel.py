from karel.stanfordkarel import *

def main():
    while front_is_clear():
        fill_beepers()
        turn_west()
        next_row()


def fill_beepers():
    #pre: Karel is facing East at start of the row
    #post: Karel put beepers and is at the end of the row east
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def turn_west():
    #pre: Karel end of row facing East
    #post: Karel end of row facing West
    for i in range(2):
        turn_left()

def next_row():
    #pre:Karel is at the end of row facing West
    #post: Karel is at the start of new row
    while front_is_clear():
        move()
    climb_up()
    if front_is_clear():
        move()
        turn_east()
    else:
        turn_east()
        while front_is_clear():
            move()


def climb_up():
    #pre:Karel is facing West
    #post: Karel is facing North
    for i in range(3):
        turn_left()

def turn_east():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()