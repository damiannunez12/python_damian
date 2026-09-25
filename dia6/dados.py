import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

while True:

    if dado1 == dado2:
        print(f"Doble {dado1} - {dado2}")
    else:
        print(f"{dado1} - {dado2}") 