print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42

user_number = int(input("Try a number: "))

if (secret_number == user_number):
    print("U got it!")
else:
    print("Bad choise...")

print("Bye!")