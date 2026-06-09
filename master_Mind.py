#!/bin/python3
# MasterMind
# by ICTROCN

print("MasterMind")

import random

# Lijst met kleuren
COLORS = ["Red", "Blue", "Yellow", "Purple", "Green"]

# Laad het admin wachtwoord uit een tekstbestand
def load_Password(filename="password.txt"):
    with open(filename) as f:
        # Read leest de hele inhoud
        # Strip verwijdert eventuele regels en spaties
        # Return geeft de waarde terug aan de functie die het aanroept
        return f.read().strip()

# Laad het admin wachtwoord bij het starten van het programma
ADMIN_PASSWORD = load_Password()

def generate_Code(length=4):
    return [random.choice(COLORS) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)

    return black_Pegs, white_Pegs

# Controleer of de speler admin is
def admin_Check():
    # Verwijderd spatie na vraag input
    password = input("Enter admin password: ").strip()
    # Vergelijk de ingevoerde waarde met het geladen wachtwoord
    if password == ADMIN_PASSWORD:
        print("Access granted.")
        return True
    else:
        print("Wrong password. Access denied.")
        return False

# Toont de geheime code alleen als de speler admin is
def show_Secret(mystery, is_Admin):
    if is_Admin:
        print(f"Secret code: {mystery}")
    else:
        print("Access denied. Admin only.")

# Neemt true/false waarde mee om te bepalen of de speler admin is
# Is nodig voor de show_Secret functie
def play_Mastermind(is_Admin):
    print("Welcome to Mastermind!")
    # .join(colors) toegevoegd ivm met laten zien wat beschikbaar is
    print(f"Guess the 4 colors. Choose from: {', '.join(COLORS)}")
    print("You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        # Guess is lijst ipv string
        # Kan je kleuren mee splitsen en vergelijken
        guess = []
        valid_Guess = False;
        while not valid_Guess:
            # Kleuren toegevoegd aan de prompt
            # Laat attempt zien
            raw_input = input(f"Attempt {attempt} ({', '.join(COLORS)}): ").strip()

            # Laat de code zien als de speler admin is en cheat invult
            # lower() toegevoegd zodat het niet hoofdlettergevoelig is
            # show_Secret aangepast zodat alleen admin kan aanroepen
            if raw_input.lower() == "cheat":
                show_Secret(secret_Code, is_Admin)
                continue

            # split toegevoegd zodat je kleuren kan scheiden met spaties
            # capitalize toegevoegd zodat het niet hoofdlettergevoelig is
            guess = [color.capitalize() for color in raw_input.split()]

            valid_Guess = len(guess) == 4 and all(c in COLORS for c in guess)
            if not valid_Guess:
                print(f"Invalid input. Enter exactly 4 colors from: {', '.join(COLORS)}")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {' '.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {' '.join(secret_Code)}")

if __name__ == "__main__":
    # Print header toegevoegd voor duidelijkheid
    print("=== Admin check ===")
    # true of false waarde opgeslagen in variabele voordat het spel begint
    is_Admin = admin_Check()

    again = 'Y'
    while again == 'Y':
        # Geef de admin status mee aan de play_Mastermind functie
        play_Mastermind(is_Admin)
        again = input("Play again (Y/N) ?").upper()