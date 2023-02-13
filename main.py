import random


def Game():
    print("Hi! Let`s start a game!\nChoose the number:")
    try:
        choice = int(input("1 - start the game\n0 - read the rules\n"))
    except:
        print("\033[31m{}".format("Wrong input, try again"))



Game()
