from random import random

print("*********************************")
print("Welcome to the divination game!")
print("*********************************")

secret_number = int(random() * 100)
"Também é possível usar um round, para arredondar números quebrados round(valor)"
total_trys = 3

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
        print("U got it!")
        break
    elif (is_smaller_than):
        print("Bad choise, your try is small than secret number.")
    else:
        print("Ops, your number is so big, try another number...")
    round += 1
print("Bye!")
