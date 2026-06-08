#!/bin/python3
# MasterMind
# by ICTROCN

print("MasterMind")

import random

COLORS = ["Red", "Blue", "Yellow", "Purple", "Green"]

# Laad het admin wachtwoord uit een tekstbestand
def load_Password(filename="password.txt"):
    with open(filename) as f:
        return f.read().strip() # .strip() verwijdert enters aan het einde

ADMIN_PASSWORD = load_Password()

# Genereer een willekeurige code van 4 kleuren
def generate_Code(length=4):
    return [random.choice(COLORS) for _ in range(length)]

# Bereken hoeveel zwarte en witte pennen de speler krijgt
def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    secret_Counts = {}
    guess_Counts = {}

    # Hoe vaak elke kleur voorkomt, maar sla de juiste posities over
    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

# Controleer of de speler admin is
def admin_Check():
    password = input("Enter admin password: ").strip()
    if password == ADMIN_PASSWORD:
        print("Access granted.")
        return True
    else:
        print("Wrong password. Access denied.")
        return False

def show_Secret(mystery, is_Admin):
    if is_Admin:
        print(f"Secret code: {mystery}")
    else:
        print("Access denied. Admin only.")

# Het spel zelf
def play_Mastermind(is_Admin):
    print("Welcome to Mastermind!")
    print(f"Guess the 4 colors. Choose from: {', '.join(COLORS)}")
    print("You have 10 attempts.")

    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = []
        valid_Guess = False

        # Blijf vragen totdat de speler iets geldigs invoert
        while not valid_Guess:
            raw_input = input(f"Attempt {attempt} (Red Blue Green Red): ").strip()

            # Laat de code zien als de speler admin is
            if raw_input.lower() == "cheat":
                show_Secret(secret_Code, is_Admin)
                continue

            # Splits invoer op spaties en zet elke kleur naar hoofdletter
            guess = [color.capitalize() for color in raw_input.split()]

            # Controleer of er precies 4 geldige kleuren zijn ingevoerd
            valid_Guess = len(guess) == 4 and all(c in COLORS for c in guess)
            if not valid_Guess:
                print(f"Invalid input. Enter exactly 4 colors from: {', '.join(COLORS)}")

        # Feedback op de ingevoerde poging
        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {' '.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {' '.join(secret_Code)}")

if __name__ == "__main__":
    print("=== Admin check ===")
    is_Admin = admin_Check()

    again = 'Y'
    while again == 'Y':
        play_Mastermind(is_Admin)
        again = input("Play again (Y/N) ?").upper()