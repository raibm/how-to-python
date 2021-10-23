import random


def play():
    show_initial_message()
    secret_word = set_secret_word()
    right_letters = prepare_secret_word(secret_word)

    got_it = False
    hanged = False
    wrongs_letters = 0

    while (not got_it and not hanged):
        print(right_letters)
        guess = input("Try a letter")
        guess = guess.strip().lower()  # The function 'strip()' may be used not only remove blank characters, but special characters too
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


def show_initial_message():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")


def set_secret_word():
    with open("words.txt", "r") as words:
        secret_words = [line.strip() for line in words]
    # words.close() is not more needed, because the key word 'with' do it
    return secret_words[random.randrange(0, len(secret_words))].lower()


def prepare_secret_word(word):
    return ["_" for letter in word]


if (__name__ == "__main__"):
    play()
