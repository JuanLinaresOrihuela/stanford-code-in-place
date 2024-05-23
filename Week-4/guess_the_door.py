def main():
    door = int(input("Door: "))  # Get user input for a door number
    
    while door < 1 or door > 3 :  # While the input is invalid 
       print("Invalid door!")  # Tell the user the input was invalid
       door = int(input("Door: "))  # Ask the user for a new input
    
    # Make an initial prize, we'll update it later based on which door is chosen!
    prize = 4
    
    # Pick a prize based on the door number
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        locked = prize % 2 != 0  # If prize isn't an even number, the door is locked
        if not locked:
            prize += 6
    elif door == 3 :
        for i in range(door):
            prize += i

    print("You win", prize, "prizes")

if __name__ == '__main__':
    main()