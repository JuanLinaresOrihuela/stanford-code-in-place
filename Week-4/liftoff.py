"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():
    for i in reversed(range(10)):
        print(i + 1)
    print("Liftoff!")


if __name__ == '__main__':
    main()