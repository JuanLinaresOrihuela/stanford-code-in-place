import random

def main():
    num_dice_sides = int(input("How many does your dice have? "))
    roll_number = random.randint(1, num_dice_sides)
    print("Your roll was " + str(roll_number))

if __name__ == '__main__':
    main()