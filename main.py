import random

gestures = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

def result(player_gesture,pc_gesture,player_name):
    print(gestures[player_gesture] + "\tvs\t" + gestures[pc_gesture])
    if((player_gesture == 1 and pc_gesture in (3,4)) or (player_gesture == 2 and pc_gesture in (1,5)) or
            (player_gesture == 3 and pc_gesture in (2,4)) or (player_gesture == 4 and pc_gesture in (2,5)) or
            (player_gesture == 5 and pc_gesture in (1,3))):
        return player_name + " wins!Congratulations!"
    else:
        return player_name + " lost. Unfortunately! Try again)"
