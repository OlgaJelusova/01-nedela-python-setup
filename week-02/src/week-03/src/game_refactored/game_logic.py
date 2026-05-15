import random

from input_utils import get_number


def start_game():
    """
    Galvenā spēles loģika.
    """

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10

    print("Es iedomājos skaitli no 1 līdz 100.")

    while attempts < max_attempts:

        guess = get_number()

        attempts += 1

        if guess == secret_number:
            print("Pareizi!")
            break

        elif guess > secret_number:
            print("Par lielu")

        else:
            print("Par mazu")

    print(f"Pareizais skaitlis bija: {secret_number}")
    print(f"Mēģinājumu skaits: {attempts}")