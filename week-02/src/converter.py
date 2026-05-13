# === KONSTANTES ===
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020


# === IZVĒLE ===
print("Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) USD <-> EUR")

choice = input("Tava izvēle: ")

# === VIRZIENS ===
print("Virziens:")
print("1) uz priekšu")
print("2) atpakaļ")

direction = input("Tavs virziens: ")

# === IEVADES VĒRTĪBA ===
value_input = input("Ievadi skaitli: ")

# pārbaudām, vai skaitlis
try:
    value = float(value_input)
except:
    print("Kļūda: jāievada skaitlis!")
    exit()


# === APRĒĶINS ===

if choice == "1":
    if direction == "1":
        result = value * KM_TO_MI
        print(f"{value:.2f} km = {result:.2f} mi")
    else:
        result = value / KM_TO_MI
        print(f"{value:.2f} mi = {result:.2f} km")

elif choice == "2":
    if direction == "1":
        result = value * KG_TO_LB
        print(f"{value:.2f} kg = {result:.2f} lb")
    else:
        result = value / KG_TO_LB
        print(f"{value:.2f} lb = {result:.2f} kg")

elif choice == "3":
    if direction == "1":
        result = value * L_TO_GAL
        print(f"{value:.2f} L = {result:.2f} gal")
    else:
        result = value / L_TO_GAL
        print(f"{value:.2f} gal = {result:.2f} L")

elif choice == "4":
    if direction == "1":
        result = value * USD_TO_EUR
        print(f"{value:.2f} USD = {result:.2f} EUR")
    else:
        result = value / USD_TO_EUR
        print(f"{value:.2f} EUR = {result:.2f} USD")

else:
    print("Nepareiza izvēle!")