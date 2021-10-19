def play():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")

    secret_word = "banana"
    right_letters = ["_", "_", "_", "_", "_", "_"]

    got_it = False
    hanged = False

    print(right_letters)

    while (not got_it and not hanged):
        guess = input("Try a letter")
        guess = guess.strip()
        index = 0

        for letter in secret_word:
            if (guess.lower() == letter.lower()):
                right_letters[index] = letter
                index = index + 1
                continue
            index = index + 1
        print(right_letters)

if (__name__ == "__main__"):
    play()
