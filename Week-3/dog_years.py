DOG_YRS_MULTIPLIER = 7.18  

def main():
    calendar_years = int(input("Enter an age in calendar years: "))
    dog_to_human = calendar_years * DOG_YRS_MULTIPLIER
    print("That's " + str(dog_to_human) + " in dog years!")


if __name__ == '__main__':
    main()