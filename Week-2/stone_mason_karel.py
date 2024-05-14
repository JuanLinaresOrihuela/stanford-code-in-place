from karel.stanfordkarel import *

def main():
    first_column_beeper_placing()
    move_between_columns()
    second_column_beeper_placing()
    move_between_columns()
    third_column_beeper_placing()
    move_between_columns()
    fourth_column_beeper_placing()
    to_the_end()


def first_column_beeper_placing():
    turn_left()
    put_beeper()
    column_beeper_placing()

def second_column_beeper_placing():
    turn_left()
    put_beeper()
    column_beeper_placing()

def third_column_beeper_placing():
    turn_left()
    put_beeper()
    column_beeper_placing()

def fourth_column_beeper_placing():
    turn_left()
    put_beeper()
    column_beeper_placing()

def move_between_columns():
    turn_left()
    turn_left()
    move_four_places()
    turn_left()
    move_four_places()

def move_four_places():
    move()
    move()
    move()
    move()

def to_the_end():
    turn_left()
    turn_left()
    move_four_places()
    turn_left()

def column_beeper_placing():
    while front_is_clear():
        move()
        put_beeper()



if __name__ == '__main__':
    main()