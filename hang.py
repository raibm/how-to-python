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
                show_won_game_message()
        else:
            wrongs_letters += 1
            draw_hang(wrongs_letters)
            hanged = wrongs_letters == 7
            if (hanged):
                show_lost_game_message(secret_word)


def show_initial_message():
    print("*********************************")
    print("Welcome to the gibble game!")
    print("*********************************")


def show_lost_game_message(secret_word):
    print("You got hanged!")
    print("The secret word is {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def draw_hang(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def show_won_game_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


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
