def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    correct_count = 0 
    total_words = len(translations) 
    keys = list(translations.keys())

    for i, key in enumerate(keys):
        value = translations[key]
        x = input("What is the Spanish translation for " + str(key) + "? ")
        if x == str(translations[key]): 
            print("That is correct!")
            correct_count += 1  
        else: 
            print("That is incorrect, the Spanish translation for " + str(key) + " is " + str(translations[key]) + ".")
        print()
        if i == len(keys) - 1:
            print("You got " + str(correct_count) + "/" + str(total_words) + " words correct, come study again soon!")

if __name__ == '__main__':
    main()
