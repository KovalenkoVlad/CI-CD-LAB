from random import randint


def Game():  # this function invites player to the game and generates random result of second player-bot

    print("Enter your name: ")
    player_name = input()
    print("%s, choose a gesture:" % player_name)
    try:
        number_of_gesture = int(
            input("1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n"))  # player chooses a gesture
        if number_of_gesture in (1, 2, 3, 4, 5):
            bot_gesture = randint(1, 5)  # bot generates a random gesture
            result(number_of_gesture, bot_gesture, player_name)
        else:
            print("\033[31m{}".format(
                "You choose a wrong number, try again"))  # case in which player chose a wrong number of gesture
    except:
        print("\033[31m{}".format("Wrong input, try again"))  # case in which player entered a wrong input


Game()
