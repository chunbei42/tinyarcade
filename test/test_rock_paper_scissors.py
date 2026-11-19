from tinyarcade.game_rock_paper_scissors import decide_winner


def test_rock_beats_scissors():
    assert decide_winner("rock", "scissors") == "player"


def test_paper_beats_rock():
    assert decide_winner("paper", "rock") == "player"


def test_scissors_beat_paper():
    assert decide_winner("scissors", "paper") == "player"


def test_same_choices_are_tie():
    assert decide_winner("rock", "rock") == "tie"
    assert decide_winner("paper", "paper") == "tie"
    assert decide_winner("scissors", "scissors") == "tie"


def test_computer_wins_when_player_loses():
    assert decide_winner("rock", "paper") == "computer"
    assert decide_winner("paper", "scissors") == "computer"
    assert decide_winner("scissors", "rock") == "computer"