def play():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")

    secret_word = "banana"
    got_it = False
    hanged = False

    while(not got_it and not hanged):
        guess = input("Try a letter")
        guess = guess.strip()

        print(secret_word.format_map(secret_word, "_"))

        for letter in secret_word:
            index = 0
            if(guess.lower() == letter.lower()):
                guess.whitespace()
                print("Got it!")


if (__name__ == "__main__"):
    play()
