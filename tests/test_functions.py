import pytest
from main import lose, win, tie, result, Game, wrong_number


def test_lose_message():
    assert lose() == "You lost. Unfortunately! Try again)"


def test_win_message():
    assert win() == "You win!Congratulations!"


def test_tie_message():
    assert tie() == "Tie"


def test_exception_message():
    with pytest.raises(BaseException):
        Game()


def test_wrong_number_message():
    assert wrong_number() == "\033[31m{}".format(
        "You have chosen a wrong number, try again")


@pytest.mark.parametrize('player_gesture, pc_gesture, results', [(1, 2, "You lost. Unfortunately! Try again)"),
                                                                 (1, 3, "You win!Congratulations!"),
                                                                 (2, 5, "You win!Congratulations!"),
                                                                 (4, 4, "Tie"),
                                                                 (5, 3, "You win!Congratulations!"),
                                                                 (3, 5, "You lost. Unfortunately! Try again)"),
                                                                 (5, 5, "Tie"),
                                                                 (4, 5, "You win!Congratulations!"),
                                                                 (2, 4, "You lost. Unfortunately! Try again)"),
                                                                 (1, 4, "You win!Congratulations!"),
                                                                 (1, 5, "You lost. Unfortunately! Try again)")])
def test_result(player_gesture, pc_gesture, results):
    assert result(player_gesture, pc_gesture) == results
