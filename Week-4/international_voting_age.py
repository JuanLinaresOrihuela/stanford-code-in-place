PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    user_age = int(input("How old are you? "))
    
    if user_age >= 48:
        print("You can vote in Peturksbouipo where the voting age is 16.") 
        print("You can vote in Stanlau where the voting age is 25.")
        print("You can vote in Mayengua where the voting age is 48.")
    elif user_age >= 25:
        print("You cannot vote in Peturksbouipo where the voting age is 16.") 
        print("You can vote in Stanlau where the voting age is 25.")
        print("You can vote in Mayengua where the voting age is 48.")
    elif user_age >=16:
        print("You can vote in Peturksbouipo where the voting age is 16.") 
        print("You cannot vote in Stanlau where the voting age is 25.")
        print("You cannot vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.") 
        print("You cannot vote in Stanlau where the voting age is 25.")
        print("You cannot vote in Mayengua where the voting age is 48.")
        

if __name__ == '__main__':
    main()