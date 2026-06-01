#!/bin/python3
# tafel.py

keuze = int(input("Welke tafel? (1-10): "))

for i in range(1, 11):  # 1 t/m 10
    print(keuze, "x", i, "=", keuze * i)
