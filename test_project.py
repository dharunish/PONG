import pytest

from project.project import move_up
from project.project import move_down, HEIGHT, LENGTH_PLAYER
from project.project import end_game

def test_move_up():
    assert move_up(100) == 95
    assert move_up(5) == 0
    assert move_up(3) == 0



def test_move_down():
    assert move_down(50) == 55
    assert move_down(HEIGHT-LENGTH_PLAYER) == HEIGHT - LENGTH_PLAYER
    assert move_down((HEIGHT-LENGTH_PLAYER)+10) == HEIGHT - LENGTH_PLAYER




def test_end_game():
    score1, score2, state, text = end_game(5, 1, "play", "")
    assert score1 ==  0 and score2 == 0 and state == "end"
    score1, score2, state, text = end_game(1, 1, "play", "")
    assert score1 == 1 and score2 == 1 and state == "play"
    score1, score2, state, text = end_game(1, 5, "play", "")
    assert score1 == 0 and score2 == 0 and state == "end"






