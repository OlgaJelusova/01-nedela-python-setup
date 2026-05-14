import random
while True:
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10

    print("Es iedomājos skaitli no 1 līdz 100.")

    while attempts < max_attempts:

        try:
            guess = int(input("Tavs minējums: "))

        except ValueError:
            print("Lūdzu ievadi skaitli!")
            continue

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

    play_again = input("Vai gribi spēlēt vēlreiz? (j/n): ")

    if play_again != "j":
        print("Paldies par spēli!") 
        break