def play():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")

    secret_word = "banana".lower()
    right_letters = ["_", "_", "_", "_", "_", "_"]

    got_it = False
    hanged = False
    wrongs_letters = 0

    print(right_letters)

    while (not got_it and not hanged):
        guess = input("Try a letter")
        guess = guess.strip().lower()
        index = 0

        if (guess in secret_word and wrongs_letters < len(secret_word)):
            for letter in secret_word:
                if (guess == letter):
                    right_letters[index] = letter
                index = index + 1
        else:
            wrongs_letters += 1
            hanged = wrongs_letters == len(secret_word)
            got_it = "_" not in right_letters
            print("errrrouuu: ",wrongs_letters)


if (__name__ == "__main__"):
    play()
