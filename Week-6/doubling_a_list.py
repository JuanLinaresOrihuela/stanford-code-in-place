numbers = [1,2,3,4]

def main():
    for i in range(len(numbers)):
        element_at_index = numbers[i]
        numbers[i] = 2 * element_at_index
    print(numbers)

if __name__ == '__main__':
    main()