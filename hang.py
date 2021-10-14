def play():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")

    secret_word = "banana"
    got_it = False
    hanged = False

    while(not got_it and not hanged):
        guess = input("Try a letter")

        for letter in secret_word:
            if(guess.lower() == letter.lower()):
                print("Got it!")


if (__name__ == "__main__"):
    play()
