while True:
    age = int(input("Ievadi savu vecumu (0 lai iziet): "))

    if age == 0:
        print("Programma beidzas")
        break

    if age < 0:
        print("Nepareizs vecums")
    elif age < 18:
        print("Tu vēl nevari balsot")
    elif age <= 120:
        print("Tu vari balsot")
    else:
        print("Vecums izskatās nereāls")