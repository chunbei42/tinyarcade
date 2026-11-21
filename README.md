# tinyarcade

A tiny collection of terminal mini-games with a shared menu.

TinyArcade runs entirely in the terminal and includes six games: Number Guess, Mastermind, Tic-Tac-Toe, Colour Memory Challenge, Rock-Paper-Scissors, and Hangman. Choose a game from the main menu, play it, then return to the menu or quit.

Install:

```bash
pip install tinyarcade
```

PyPI: https://pypi.org/project/tinyarcade/

Repository: https://github.com/chunbei42/tinyarcade

## Requirements

- Python >= 3.9
- A terminal that supports ANSI colour output

TinyArcade has no external Python dependencies.

## Install

```bash
pip install tinyarcade
```

## Uninstall

```bash
pip uninstall tinyarcade
```

## Usage

Start TinyArcade from the terminal:

```bash
tinyarcade
```

You can also start it from Python:

```python
from tinyarcade.menu import run

run()
```

The main menu lets you choose one of the available games:

```text
=== TinyArcade ===
1. Number Guess
2. Mastermind
3. Tic Tac Toe
4. Colour Memorizing
5. Rock, Paper, Scissors
6. Hangman
q. Quit
```

Enter the number beside a game to play it. Enter `q` to leave TinyArcade.

## Games

### Number Guess

Guess a secret number between 1 and 1,000.

After every incorrect guess, the possible range becomes smaller. The game tells you whether your guess was too high or too low, and tracks the number of attempts.

### Mastermind

Break a hidden numeric code.

Choose a difficulty, then enter guesses of the correct length. After each guess, the game reports:

- **Digits**: how many digits in your guess appear in the secret code
- **Positions**: how many digits are both correct and in the correct position

Easy uses 3 digits, Normal uses 4, and Hard uses 6. Hints are available on Normal and Hard.

### Tic-Tac-Toe

Play Tic-Tac-Toe against another person or the computer.

- **PVE**: play against the computer
- **PVP**: play against another player

The computer has three difficulty levels:

- **Easy**: makes random moves
- **Normal**: wins when possible and blocks opponent wins
- **Hard**: uses a minimax search to play a strong move

Enter a position from 1 to 9 to place your mark.

### Colour Memory Challenge

Memorise and repeat a growing sequence of coloured squares.

At the start, the sequence uses red, blue, and green. Yellow, white, and purple are introduced at later stages.

Watch the sequence, then enter it using letter keys:

| Key | Colour |
|---|---|
| `r` | Red |
| `b` | Blue |
| `g` | Green |
| `y` | Yellow |
| `w` | White |
| `p` | Purple |

The sequence grows by one colour each stage. Enter the full sequence in order to advance. Press `q` during input to return to the menu.

### Rock, Paper, Scissors

Play Rock, Paper, Scissors against the computer.

Choose one of three difficulty modes:

- **Easy**: win one round
- **Normal**: first player to win three rounds
- **Hard**: win three rounds in a row

Enter `1` for rock, `2` for paper, or `3` for scissors. The game displays both choices, updates the scoreboard, and shows the round result.

### Hangman

Guess a hidden word one letter at a time.

Choose a difficulty:

- **Easy**: 5 hints
- **Normal**: 3 hints
- **Hard**: no hints

Type a letter to guess it, or type `hint` to reveal a letter that is not in the word. You may make up to six incorrect guesses before the game ends.

## Controls

Most games use keyboard input only.

- Enter numbers or letters when prompted
- Press `q` where available to quit a game or return to the menu
- Press `ENTER` to continue after prompts
- Choose from numbered options in game menus

## Development

Clone the repository and install the package in editable mode:

```bash
git clone [https://github.com/chunbei42/tinyarcade.git](https://github.com/chunbei42/tinyarcade.git)
cd tinyarcade
python -m pip install -e .
```

Run TinyArcade during development:

```bash
tinyarcade
```

Build distribution files:

```bash
python -m pip install --upgrade build
python -m build
```

The package uses the `src/` layout:

```text
tinyarcade/
├── LICENSE
├── README.md
├── pyproject.toml
└── src/
    └── tinyarcade/
        ├── __init__.py
        ├── menu.py
        ├── game_num_guess.py
        ├── game_mastermind.py
        ├── game_tictactoe.py
        ├── game_colour_memorizing.py
        ├── game_rock_paper_scissors.py
        └── game_hangman.py
```

## License

TinyArcade is released under the [MIT License](LICENSE).
