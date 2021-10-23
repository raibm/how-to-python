def play():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")

    secret_word = "banana".lower()
    right_letters = ["_" for letter in secret_word]

    got_it = False
    hanged = False
    wrongs_letters = 0

    while (not got_it and not hanged):
        print(right_letters)
        guess = input("Try a letter")
        guess = guess.strip().lower()
        index = 0

        if (guess in secret_word and wrongs_letters < len(secret_word)):
            for letter in secret_word:
                if (guess == letter):
                    right_letters[index] = letter
                index = index + 1
            got_it = "_" not in right_letters
            if (got_it):
                print("You got it! That's the word:", secret_word)
        else:
            wrongs_letters += 1
            hanged = wrongs_letters == len(secret_word)
            if (hanged):
                print("You are hanged!")


if (__name__ == "__main__"):
    play()
