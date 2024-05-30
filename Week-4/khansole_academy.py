import random

def main():
    # Random numbers
    print("Khansole Academy")
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    print("What is " + str(num1) + " + " + str(num2) + "?")
    
    # User input
    user_input_str = input("Your answer: ")
    user_input_int = int(user_input_str)
    print(user_input_int)
    
    # Verify math
    correct_math = num1 + num2
    
    # Verify answer
    if user_input_int != correct_math:
        print("Incorrect.")
        print("The expected answer is " + str(correct_math)) # Here added the correct answer for the user.
    else:
        print("Correct.")
    
if __name__ == '__main__':
    main()