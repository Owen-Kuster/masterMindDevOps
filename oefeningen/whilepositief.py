#!/bin/python3
# whilepositief.py

getal = 1  # beginwaarde — waarom NIET 0?

while getal != 0:
    getal = int(input("Getal (0 = stop): "))
    if getal >= 0:
        print("Top! Dat is positief.")
    elif getal <= 0:
        print("Dat is negatief.")
