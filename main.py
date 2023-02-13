import random
from PIL import Image

gestures = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

def result(player_gesture,pc_gesture,player_name):
    print(gestures[player_gesture] + "\tvs\t" + gestures[pc_gesture])
    if((player_gesture == 1 and pc_gesture in (3,4)) or (player_gesture == 2 and pc_gesture in (1,5)) or
            (player_gesture == 3 and pc_gesture in (2,4)) or (player_gesture == 4 and pc_gesture in (2,5)) or
            (player_gesture == 5 and pc_gesture in (1,3))):
        return player_name + " wins!Congratulations!"
    else:
        return player_name + " lost. Unfortunately! Try again)"



play = input("Do you want to start a game of Rock Paper Scissors Lizard Spock? If yes, please enter y : ")
rules = input("Do you want to read the rules?  If yes, please enter y : ")
if(rules.lower() == 'y'):
    image_rules = input("If you want to see a visual instruction enter y :")
    try:
        with open("Rules of the game.txt") as file:
            print(file.read())
        if(image_rules.lower() == 'y'):
            img = Image.open(r'photo_2023-02-13_19-30-47.jpg')
            img.show()
    except:
        pass

if(play.lower() == 'y'):
    Game()
else:
    print("See you next time. Goodbye)")