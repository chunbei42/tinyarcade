# tinyarcade

A tiny collection of terminal mini-games with a shared menu.

TinyArcade runs entirely in the terminal and includes six games: Number Guess, Mastermind, Tic-Tac-Toe, Colour Memory Challenge, Rock-Paper-Scissors, and Hangman. Choose a game from the main menu, play it, then return to the menu or quit.

Install:

```bash
pip install tinyarcade
```

PyPI: https://pypi.org/project/tinyarcade/

Repository: https://github.com/chunbei42/tinyarcade

## Why TinyArcade?

TinyArcade was created to make a small collection of classic terminal games easy to run from one place. Instead of opening separate scripts or remembering different commands for each game, users can install one package and launch every game from a shared menu.

The project is designed to be simple, lightweight, and beginner-friendly. It uses only Python’s standard library, so it can run without installing extra dependencies. It is also a practical example of packaging a command-line application with a `src/` layout, a console entry point, and a shared menu system.

## What makes it different?

TinyArcade is not just one game—it is a small arcade with a consistent interface.

- **One command, six games:** `tinyarcade` opens a shared menu where users can choose a game.
- **No external dependencies:** all games use Python’s standard library, making installation and maintenance simple.
- **Consistent controls:** games use numbered menus, keyboard input, and a common way to return to the main menu.
- **Colourful terminal output:** games use ANSI colours to make boards, sequences, and results easier to read.
- **Different difficulty levels:** several games include Easy, Normal, and Hard modes.
- **Reusable game structure:** every game exposes a `play()` function, allowing the shared menu to launch any game in the same way.

The package is intentionally small, but its structure makes it easy to add more games later. A new game only needs a `play()` function and an entry in the menu’s `GAMES` dictionary.

## Example use cases

### Learning Python packaging

TinyArcade can be used as a compact example of building and distributing a Python command-line package. It demonstrates:

- A `src/` package layout
- A `pyproject.toml` build configuration using Hatchling
- A console-script entry point
- A shared menu that imports and calls game modules
- A package that can be installed with `pip`

For example, after installing the package, a user can start it with:

```bash
tinyarcade
```

### Playing quick games

TinyArcade is useful for short breaks or casual play. A user can open a terminal, run `tinyarcade`, choose a game, play for a few minutes, and return to the menu.

Examples include:

- Guessing a number in **Number Guess**
- Solving a hidden code in **Mastermind**
- Playing a quick match of **Rock, Paper, Scissors**
- Testing memory in **Colour Memory Challenge**
- Playing a round of **Tic-Tac-Toe** with a friend
- Guessing a word in **Hangman**

### Practising logic and strategy

Some games give players a chance to practise different skills:

| Game | Skill practised |
|---|---|
| Number Guess | Logical narrowing of a range |
| Mastermind | Deduction and pattern recognition |
| Tic-Tac-Toe | Strategy and planning ahead |
| Colour Memory Challenge | Memory and attention |
| Rock, Paper, Scissors | Probability and decision-making |
| Hangman | Vocabulary and letter-frequency reasoning |

### Demonstrating terminal applications

TinyArcade can be used to show how a Python package can provide an interactive terminal experience. It is suitable for a class demonstration, a small portfolio project, or an example of how multiple Python modules can work together behind one command-line interface.

For example, a teacher could use it to demonstrate:

- How a console command is created with `[project.scripts]`
- How modules in a package communicate through imports
- How a menu can call different functions dynamically
- How a project can be organised with a `src/` layout
- How a package can be built and installed locally

## Requirements

- Python >= 3.9
- A terminal that supports ANSI colour output

TinyArcade has no external Python dependencies.

## Setup

### Install from PyPI

```bash
pip install tinyarcade
```

### Install from source

Clone the repository and install it in editable mode:

```bash
git clone [https://github.com/chunbei42/tinyarcade.git](https://github.com/chunbei42/tinyarcade.git)
cd tinyarcade
python -m pip install -e .
```

### Run TinyArcade

After installation, start the arcade from the terminal:

```bash
tinyarcade
```

Or start it from Python:

```python
from tinyarcade.menu import run

run()
```

## Usage

When TinyArcade starts, choose a game by entering its number:

```text
==================================================
                  🎮 TINYARCADE 🎮                  
                  Select a Game                   
==================================================

 [1] Number Guess
 [2] Mastermind
 [3] Tic Tac Toe
 [4] Colour Memorizing
 [5] Rock, Paper, Scissors
 [6] Hangman
 [Q] Quit

==================================================
👉 Enter your choice: 
```

For example, enter `3` to play Tic-Tac-Toe:

```text
👉 Enter your choice: 3
```

After finishing a game, you will return to the TinyArcade menu and can choose another game.

Enter `q` at the main menu to quit. TinyArcade will show a goodbye message before closing:

```text
==================================================
              THANK YOU FOR PLAYING               
                    TINYARCADE                    
==================================================

               🎮 Hope you had fun!                
    🏆 Keep practicing and challenge yourself!     
       🕹️ Thanks for supporting TinyArcade!       

==================================================

Press Enter to exit...
```

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

After a game ends, choose whether to start another game, return to the TinyArcade menu, or exit.

### Colour Memory Challenge

Memorise and repeat a growing sequence of coloured squares.

At the start, the sequence uses red, blue, and green. Yellow, white, and purple are introduced at later stages.

Watch the sequence, then enter it using letter keys:

| Key | Colour |
|---|---|
| `R` | Red |
| `B` | Blue |
| `G` | Green |
| `Y` | Yellow |
| `W` | White |
| `P` | Purple |

The sequence grows by one colour each stage. Enter the full sequence in order to advance. Press `q` during input to return to the menu.

### Rock, Paper, Scissors

Play Rock, Paper, Scissors against the computer.

Choose one of three difficulty modes:

- **Easy**: win one round
- **Normal**: first player to win three rounds
- **Hard**: win three rounds in a row

Enter `1` for rock, `2` for paper, or `3` for scissors. The game displays both choices, updates the scoreboard, and shows the round result.

In Easy and Normal modes, each round win adds one point. In Hard mode, a tie resets both winning streaks, while a win by either player resets the other player’s streak.

After a match ends, choose whether to play again or return to the TinyArcade menu.

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

## Adding a game

TinyArcade is designed to be extendable. To add a new game:

1. Create a new module in `src/tinyarcade/`, such as `game_quiz.py`.
2. Define a no-argument function called `play()`.
3. Import the module in `menu.py`.
4. Add it to the `GAMES` dictionary.

Example:

```python
from tinyarcade import game_quiz

GAMES = {
    "7": ("Quiz", game_quiz.play),
}
```

The menu can then launch the new game through the same interface used by the existing games.

## License

TinyArcade is released under the [MIT License](LICENSE).
