import random


def play():
    print("*********************************")
    print("Welcome to the divination game!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    "Também é possível usar um round, para arredondar números quebrados round(int(random() * 100))"
    total_trys = 0
    difficulty_selected = False
    difficulty = 0
    total_score = 1000
    current_score = 1000
    lost_score = 0

    print("Select difficulty: ")
    while (difficulty_selected == False):
        difficulty = int(input("(1) Easy (2) Normal (3) Hard"))
        if (difficulty == 1):
            total_trys = 20
            print("Difficulty selected: Easy")
            break
        elif (difficulty == 2):
            total_trys = 10
            print("Difficulty selected: Normal")
            break
        elif (difficulty == 3):
            total_trys = 5
            print("Difficulty selected: Hard")
            break
        else:
            print("Wrong input, try another option.")

    for round in range(1, total_trys + 1):
        print("Try number {} of {}".format(round, total_trys))
        user_number = int(input("Input a number between 1 and 100: "))
        print("\n")

        if (user_number < 1 or user_number > 100):
            print("Wrong value, value must be greater or equal than 1 and smaller or equal than 100.")
            continue

        got_it = secret_number == user_number;
        is_smaller_than = user_number < secret_number;

        if (got_it):
            print("Congratulatios! u got it, the right number is {}".format(secret_number))
            break
        elif (is_smaller_than):
            print("Bad choise, your try is small than secret number.")
            lost_score = abs(secret_number - user_number)
            current_score = current_score - lost_score
        else:
            print("Ops, your number is so big, try another number...")
            lost_score = abs(user_number - secret_number)
            current_score = current_score - lost_score
        round += 1
    print("Bye! \nTotal score: {} of {}".format(current_score, total_score))


if (__name__ == "__main__"):
    play()
