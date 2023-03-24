from random import randint
from PIL import Image

gestures = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}


def Game():
    """this function invites player to the game and generates random result of second player-bot."""
    print("Choose a gesture:")
    try:
        print("1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock")
        number_of_gesture = int(input())  # player chooses a gesture
        if number_of_gesture in (1, 2, 3, 4, 5):
            bot_gesture = randint(1, 5)  # bot generates a random gesture
            print(gestures[number_of_gesture] + "\tvs\t" + gestures[bot_gesture])
            print(result(number_of_gesture, bot_gesture))
        else:
            return wrong_number()  # case in which player chose a wrong number of gesture
    except:
        print("\033[31m{}".format("Wrong input, try again"))  # case in which player entered a wrong input
        raise


def wrong_number():
    return ("\033[31m{}".format(
        "You have chosen a wrong number, try again"))


def tie():
    return "Tie"


def win():
    return "You win!Congratulations!"


def lose():
    return "You lost. Unfortunately! Try again)"


def result(player_gesture, pc_gesture):
    """This function checks conditions and returns the result of the game.
    :param player_gesture: The number of the gesture chosen by the player
    :type player_gesture: int
    :param pc_gesture: Gesture number generated by the computer
    :type pc_gesture: int

    :return: The result of the game"""

    if player_gesture == pc_gesture:
        return tie()
    if ((player_gesture == 1 and pc_gesture in (3, 4)) or (player_gesture == 2 and pc_gesture in (1, 5)) or
            (player_gesture == 3 and pc_gesture in (2, 4)) or (player_gesture == 4 and pc_gesture in (2, 5)) or
            (player_gesture == 5 and pc_gesture in (1, 3))):
        return win()
    else:
        return lose()


if __name__ == '__main__':
    play = input("Do you want to start a game of Rock Paper Scissors Lizard Spock? If yes, please enter y : ")
    rules = input("Do you want to read the rules?  If yes, please enter y : ")
    if rules.lower() == 'y':
        image_rules = input("If you want to see a visual instruction enter y :")
        try:
            with open("Rules of the game.txt") as file:
                print(file.read())
            if image_rules.lower() == 'y':
                img = Image.open(r'photo_2023-02-13_19-30-47.jpg')
                img.show()
        except:
            pass

    if play.lower() == 'y':
        Game()
    else:
        print("See you next time. Goodbye)")
