try:
    age = int(input("Ievadi vecumu: "))

    if age < 0:
        print("Kļūda: vecums nevar būt negatīvs.")
        exit()

except ValueError:
    print("Kļūda: vecumam jābūt skaitlim.")
    exit()


license_answer = input("Vai ir autovadītāja apliecība? (j/n): ").lower()
student_answer = input("Vai ir students? (j/n): ").lower()
veteran_answer = input("Vai ir veterāns? (j/n): ").lower()

has_license = license_answer == "j"
is_student = student_answer == "j"
is_veteran = veteran_answer == "j"


can_vote = age >= 18
can_rent_car = age >= 21 and has_license
senior_discount = age >= 65 or is_veteran
student_discount = 16 <= age <= 26 and is_student


print("---")
print(f"Balsošana:        {'Jā ✓' if can_vote else 'Nē ✗'}")

if can_rent_car:
    print("Auto īre:         Jā ✓")
else:
    if age < 21:
        print("Auto īre:         Nē ✗ (vecums ir mazāks par 21)")
    elif not has_license:
        print("Auto īre:         Nē ✗ (nav apliecības)")

print(f"Senioru atlaide:  {'Jā ✓' if senior_discount else 'Nē ✗'}")
print(f"Studentu atlaide: {'Jā ✓' if student_discount else 'Nē ✗'}")