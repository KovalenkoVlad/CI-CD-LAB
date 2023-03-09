from main import lose,win,tie

def test_lose_message():
    assert lose() == "You lost. Unfortunately! Try again)"

def test_win_message():
    assert win() == "You win!Congratulations!"

def test_tie_message():
    assert tie() == "Tie"