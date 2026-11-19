import os
import random
import time

# =====================================
# COLOUR MEMORY CHALLENGE
# =====================================

GAME_NAME = "COLOUR MEMORY CHALLENGE"
MAX_STAGE = 20
HEADER_WIDTH = 50

# ANSI colours
COLOURS = {
    "r": ("\033[91m", "Red"),
    "b": ("\033[94m", "Blue"),
    "g": ("\033[92m", "Green"),
    "y": ("\033[93m", "Yellow"),
    "w": ("\033[97m", "White"),
    "p": ("\033[95m", "Purple"),
}

RESET = "\033[0m"

NEW_COLOURS = {
    6: ("y", "Yellow"),
    11: ("w", "White"),
    16: ("p", "Purple"),
}


# =====================================
# UTILITIES
# =====================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def colour_text(letter):
    return f"{COLOURS[letter][0]}{letter.upper()}{RESET}"


def colour_letter(letter):
    return f"{COLOURS[letter][0]}{letter.upper()}{RESET}"


def colour_name_text(letter):
    return f"{COLOURS[letter][0]}{COLOURS[letter][1]}{RESET}"


def colour_sequence_text(sequence):
    if not sequence:
        return ""

    coloured = []

    for letter in sequence:
        if letter.lower() in COLOURS:
            coloured.append(colour_letter(letter.lower()))
        else:
            coloured.append(letter)

    return " ".join(coloured)


def print_header(stage=None):

    if stage is None:
        print(GAME_NAME)
        print("=" * HEADER_WIDTH)
        return

    stage_text = f"STAGE {stage}"

    spaces = max(
        1,
        HEADER_WIDTH - len(GAME_NAME) - len(stage_text)
    )

    print(GAME_NAME + (" " * spaces) + stage_text)
    print("=" * HEADER_WIDTH)


# =====================================
# GAME SELECTION MENU
# =====================================

def game_selection_menu():

    while True:

        clear_screen()

        print("=" * HEADER_WIDTH)
        print("GAME SELECTION")
        print("=" * HEADER_WIDTH)

        print("\n[1] Colour Memory Challenge")
        print("[2] Exit")

        choice = input("\nChoose: ").strip()

        if choice == "1":
            colour_memory_game()

        elif choice == "2":
            clear_screen()
            print("Thanks for playing!")
            return


# =====================================
# GAME DATA
# =====================================

def available_colours(stage):

    colours = ["r", "b", "g"]

    if stage >= 6:
        colours.append("y")

    if stage >= 11:
        colours.append("w")

    if stage >= 16:
        colours.append("p")

    return colours


def choose_next_colour(sequence, available):

    weights = []

    for colour in available:

        weight = 100

        # Slightly discourage repeats
        if sequence and colour == sequence[-1]:
            weight = 50

        # Triple repeats are allowed but uncommon
        if len(sequence) >= 2:
            if colour == sequence[-1] == sequence[-2]:
                weight = 20

        # Never allow four identical colours in a row
        if len(sequence) >= 3:
            if (
                colour ==
                sequence[-1] ==
                sequence[-2] ==
                sequence[-3]
            ):
                weight = 0

        # Reduce chance if colour appeared frequently recently
        recent = sequence[-5:]
        weight -= recent.count(colour) * 10

        weights.append(max(0, weight))

    return random.choices(
        available,
        weights=weights,
        k=1
    )[0]


def build_master_sequence():

    sequence = []

    for stage in range(1, MAX_STAGE + 1):

        available = available_colours(stage)

        next_colour = choose_next_colour(
            sequence,
            available
        )

        sequence.append(next_colour)

    return sequence


# =====================================
# INSTRUCTIONS
# =====================================

def show_instructions():

    clear_screen()

    print_header()

    print("\nOBJECTIVE")
    print("Memorise the sequence and enter it back")
    print("using letter keys only.")

    print("\nCOLOUR KEYS")

    print(f"{colour_text('r')} = Red")
    print(f"{colour_text('b')} = Blue")
    print(f"{colour_text('g')} = Green")

    print("\nMORE COLOURS WILL UNLOCK")

    print(f"Stage 6  → {colour_text('y')} Yellow")
    print(f"Stage 11 → {colour_text('w')} White")
    print(f"Stage 16 → {colour_text('p')} Purple")

    print("\nRULES")

    print("• Sequence grows every stage.")
    print("• Letters only.")
    print("• Spaces are ignored.")
    print("• Case-insensitive.")
    print("• Q quits to Game Selection.")

    print("\nExample")
    print(
        f"{colour_text('r')} → "
        f"{colour_text('b')} → "
        f"{colour_text('g')}"
    )
    print("Answer: RBG")

    choice = input(
        "\nPress ENTER to start or Q to quit: "
    ).strip()

    if choice.upper() == "Q":
        return False

    return True


# =====================================
# COLOUR KEYS
# =====================================

def show_colour_keys(stage):

    print("\nCOLOUR KEYS")

    print(f"{colour_text('r')} = Red")
    print(f"{colour_text('b')} = Blue")
    print(f"{colour_text('g')} = Green")

    if stage >= 6:
        print(f"{colour_text('y')} = Yellow")

    if stage >= 11:
        print(f"{colour_text('w')} = White")

    if stage >= 16:
        print(f"{colour_text('p')} = Purple")


# =====================================
# VISUALS
# =====================================

def show_dot(letter):

    colour_code = COLOURS[letter][0]

    print("\n" * 4)
    print(" " * 20 + colour_code + "●" + RESET)
    print("\n" * 4)


def countdown(stage):

    for i in range(3, 0, -1):

        clear_screen()

        print_header(stage)

        print(f"\nStarting in {i}...")

        time.sleep(1)


def show_new_colour_message(stage):

    if stage not in NEW_COLOURS:
        return

    letter, name = NEW_COLOURS[stage]

    clear_screen()

    print_header(stage)

    print("\n★ NEW COLOUR UNLOCKED ★")

    print(
        f"\n{colour_text(letter)} "
        f"{name.upper()}"
    )

    print("\nThis colour can now appear in sequences.")

    input("\nPress ENTER to continue...")


def show_sequence(sequence, stage):

    for colour in sequence:

        clear_screen()

        print_header(stage)

        show_dot(colour)

        time.sleep(1)

        clear_screen()

        print_header(stage)

        time.sleep(0.35)


# =====================================
# INPUT
# =====================================

def get_player_input(stage):

    clear_screen()

    print_header(stage)

    show_colour_keys(stage)

    print("\nEnter the sequence.")
    print("Q = Return to Game Selection")

    answer = input("\nAnswer: ").strip()

    if answer.upper() == "Q":
        return "QUIT"

    return answer.replace(" ", "").lower()


# =====================================
# END MENU
# =====================================

def show_end_menu(result):

    while True:

        clear_screen()

        print_header()

        if result["status"] == "WIN":

            print("\n🏆 CONGRATULATIONS!")
            print("You completed all 20 stages!")

        elif result["status"] == "LOSE":

            print("\n❌ GAME OVER")
            print(
                f"You reached Stage "
                f"{result['stage']}."
            )

            print("\nYour answer:")
            print(
                colour_sequence_text(
                    result["player_answer"]
                )
            )

            print("\nCorrect answer:")
            print(
                colour_sequence_text(
                    result["correct_answer"]
                )
            )

            print("\nColour sequence:")

            coloured_names = []

            for colour in result["sequence"]:
                coloured_names.append(
                    colour_name_text(colour)
                )

            print(" → ".join(coloured_names))

        print("\n[1] Play Again")
        print("[2] Return to Game Selection")

        choice = input("\nChoose: ").strip()

        if choice in ("1", "2"):
            return choice


# =====================================
# GAME LOOP
# =====================================

def play_game():

    master_sequence = build_master_sequence()

    for stage in range(1, MAX_STAGE + 1):

        show_new_colour_message(stage)

        current_sequence = master_sequence[:stage]

        countdown(stage)

        show_sequence(current_sequence, stage)

        player_answer = get_player_input(stage)

        if player_answer == "QUIT":
            return {
                "status": "QUIT"
            }

        correct_answer = "".join(current_sequence)

        if player_answer != correct_answer:

            return {
                "status": "LOSE",
                "stage": stage,
                "player_answer": player_answer,
                "correct_answer": correct_answer,
                "sequence": current_sequence
            }

        clear_screen()

        print_header(stage)

        print("\n✅ Correct!")

        if stage < MAX_STAGE:
            print(
                f"Preparing Stage "
                f"{stage + 1}..."
            )

        time.sleep(1.5)

    return {
        "status": "WIN",
        "stage": MAX_STAGE
    }


# =====================================
# MAIN GAME
# =====================================

def colour_memory_game():

    should_start = show_instructions()

    if not should_start:
        return

    while True:

        result = play_game()

        if result["status"] == "QUIT":
            return

        choice = show_end_menu(result)

        if choice == "1":
            continue

        if choice == "2":
            return


# =====================================
# START
# =====================================

if __name__ == "__main__":
    game_selection_menu()
