from tinyarcade.game_hangman import display_word


def test_word_is_hidden_initially():
    assert display_word("python", set()) == "_ _ _ _ _ _"


def test_correct_letters_are_revealed():
    assert display_word("python", {"p", "y"}) == "p y _ _ _ _"


def test_all_letters_are_revealed():
    assert display_word("cat", {"c", "a", "t"}) == "c a t"


def test_repeated_letter_does_not_break_display():
    assert display_word("banana", {"a"}) == "b _ _ a _ a"


def test_no_letters_guessed():
    assert display_word("hangman", set()) == "_ _ _ _ _ _ _"