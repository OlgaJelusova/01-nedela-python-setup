age = int(input("Ievadi savu vecumu: "))

if age < 0:
    print("Nepareizs vecums")
elif age < 18:
    print("Tu vēl nevari balsot")
    age = int(input("Ievadi savu vecumu: "))

if age < 0:
    print("Nepareizs vecums")
elif age < 18:
    print("Tu vēl nevari balsot")
elif age <= 120:
    print("Tu vari balsot")
else:
    print("Vecums izskatās nereāls")