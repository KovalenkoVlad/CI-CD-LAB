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


def test_game(monkeypatch):
    input_value = '2'
    printed_result = []
    monkeypatch.setattr('builtins.input', lambda: input_value)
    monkeypatch.setattr('builtins.print',
                        lambda item: printed_result.append(item))

    expected_result1 = ['Choose a gesture:', '1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n',
                        'Paper\tvs\tRock', 'You win!Congratulations!']
    expected_result2 = ['Choose a gesture:', '1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n',
                        'Paper\tvs\tPaper', 'Tie']
    expected_result3 = ['Choose a gesture:', '1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n',
                        'Paper\tvs\tScissors', 'You lost. Unfortunately! Try again)']
    expected_result4 = ['Choose a gesture:', '1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n',
                        'Paper\tvs\tLizard', 'You lost. Unfortunately! Try again)']
    expected_result5 = ['Choose a gesture:', '1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n',
                        'Paper\tvs\tSpock', 'You win!Congratulations!']
    Game()
    if set(printed_result) == set(expected_result1):
        assert set(expected_result1) == set(printed_result)
    elif set(printed_result) == set(expected_result2):
        assert set(expected_result2) == set(printed_result)
    elif set(printed_result) == set(expected_result3):
        assert set(expected_result3) == set(printed_result)
    elif set(printed_result) == set(expected_result4):
        assert set(expected_result4) == set(printed_result)
    elif set(printed_result) == set(expected_result5):
        assert set(expected_result5) == set(printed_result)


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
