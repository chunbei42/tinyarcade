from tinyarcade.menu import GAMES


def test_menu_contains_both_games():
    game_names = {name for name, _ in GAMES.values()}

    assert "Rock, Paper, Scissors" in game_names
    assert "Tic-Tac-Toe" in game_names


def test_every_game_has_a_play_function():
    for name, game_function in GAMES.values():
        assert callable(game_function), f"{name} is not playable"