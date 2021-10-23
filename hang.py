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
        guess = get_inputed_guess()

        if (guess in secret_word and wrongs_letters < len(secret_word)):
            got_it = got_it_secret_word(secret_word, guess, right_letters)
            if (got_it):
                show_won_game_message(secret_word)
        else:
            wrongs_letters += 1
            hanged = wrongs_letters == len(secret_word)
            if (hanged):
                show_lost_game_message()


def show_initial_message():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")


def show_lost_game_message():
    print("You are hanged!")


def show_won_game_message(secret_word):
    print("You got it! That's the word:", secret_word)


def set_secret_word():
    with open("words.txt", "r") as words:
        secret_words = [line.strip() for line in words]
    # words.close() is not more needed, because the key word 'with' do it
    return secret_words[random.randrange(0, len(secret_words))].lower()


def prepare_secret_word(word):
    return ["_" for letter in word]


def get_inputed_guess():
    guess = input("Try a letter")
    return guess.strip().lower()  # The function 'strip()' may be used not only remove blank characters, but special characters too


def got_it_secret_word(secret_word, guess, right_letters):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            right_letters[index] = letter
        index = index + 1

    return "_" not in right_letters


if (__name__ == "__main__"):
    play()
