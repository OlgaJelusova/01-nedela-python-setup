def get_number():
    """
    Droši nolasa skaitli no lietotāja.
    """

    while True:

        try:
            number = int(input("Tavs minējums: "))
            return number

        except ValueError:
            print("Lūdzu ievadi skaitli!")