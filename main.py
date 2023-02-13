from random import randint


def Game():

        print("Enter your name: ")
        player_name = input()
        print("%s, choose a gesture:" % player_name)
        try:
            number_of_gesture = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n"))
            if number_of_gesture in (1, 2, 3, 4, 5):
                bot_gesture = randint(1, 5)
                result(number_of_gesture, bot_gesture, player_name)
            else:
                print("\033[31m{}".format("You choose a wrong number, try again"))
        except:
            print("\033[31m{}".format("Wrong input, try again"))


Game()
