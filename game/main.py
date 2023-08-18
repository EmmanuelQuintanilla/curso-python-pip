#Refactorizar programa Piedra, Papel o Tijera
import random

def choice_options():
    options = ("piedra", "papel", "tijera")
    user_option  = input("Elige una opción: piedra, papel o tijera -> ")
    user_option  = user_option.lower()
   
    if not user_option in options:
        print("Lo siento esa no es un opción valida")
       # continue
        return None, None

    computer_option = random.choice(options)
    print("user option ->", user_option)
    print("computer option ->", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins, drawn):
    if user_option == computer_option:
        print("Empate")
        drawn += 1
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Ganaste!!!")
            user_wins += 1
        else:
            print("Perdiste :(")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Ganaste!!!")
            user_wins += 1
        else:
            print("Perdiste :(")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Ganaste!!!")
            user_wins += 1
        else:
            print("Perdiste :(")
            computer_wins += 1
    else:
        print("Perdiste por eleccion invalida")
    return user_wins, computer_wins, drawn

def run_game():
    computer_wins = 0
    user_wins = 0
    drawn = 0
    rounds = 1
    while True:

        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)
        print("Victorias de la computadora -> ", computer_wins)
        print("Victorias del usuario -> ", user_wins)
        print("Empates -> ", drawn)

        rounds += 1

        user_option, computer_option = choice_options()
        user_wins, computer_wins, drawn = check_rules(user_option, computer_option, user_wins, computer_wins, drawn)


        
        if computer_wins == 3:
            print("El rey del piedra, papel o tijera es.. La computadora!!!")
            break
        if user_wins == 3:
            print("El rey del piedra, papel o tijera... ERES TU!!")
            break
run_game()