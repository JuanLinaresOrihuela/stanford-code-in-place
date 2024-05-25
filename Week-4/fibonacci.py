# Constant for the max term would be 10000 per instructions"

MAX_TERM_VALUE = 10000

def main():
    current_term = 0 # Give a variable for 0 Fibonacci
    next_term = 1 # Give a variable for 1st Fibonacci
    
    while current_term <= MAX_TERM_VALUE: # It has to be less than the constant
        print(current_term) # Give Fib[0]
        term_after_next = current_term + next_term # Creates a new variable and add the current Fib[0] and next Fib[1]
        current_term = next_term # Current term Fib [0] equals next Fib[1]
        next_term = term_after_next 
        
if __name__ == '__main__':
    main()