import divination_02
import hang


def choose_game():
    print("*********************************")
    print("Choose a game! :D")
    print("*********************************")

    game = int(input("(1) Gibble (2) Divination 2"))

    if (game == 1):
        print("Playing Gibble game.")
        hang.play()
    elif (game == 2):
        print("Playing Divination 2.")
        divination_02.play()


if (__name__ == "__main__"):
    choose_game()
