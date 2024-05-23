AFFIRMATION = "I am capable of doing anything I put my mind to."

def main(): 
    # Print statement and includes the Constant
    print("Please type the following affirmation: " + AFFIRMATION)
    
    user_feedback = input() # Feeback equals the input of the user.
    while user_feedback != AFFIRMATION: # While this feedback doesn't equal the constant the while loop will keep running. 
        print("That was not the affirmation.") # Message if it's not the same or equal.
        print("Please type the following affirmation: " + AFFIRMATION) # Here message is just reinstating what we want.
        user_feedback = input() # Asking for the user input again

    print("That's right! :)") # If the feedback is equal to the Constant 
    
if __name__ == '__main__':
    main()