print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42

user_number = int(input("Try a number: "))
print("\n")

got_it = secret_number == user_number;
is_smaller_than = user_number < secret_number;

if (got_it):
    print("U got it!")
elif (is_smaller_than):
    print("Bad choise, your try is small than secret number.")
else:
    print("Ops, your number is so big, try another number...")
print("Bye!")
