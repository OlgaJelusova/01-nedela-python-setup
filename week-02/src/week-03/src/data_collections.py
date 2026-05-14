numbers = [1, 2, 3, 4, 5]

print("Sākuma saraksts:", numbers)

numbers.append(6)

print("Pēc append:", numbers)


removed = numbers.pop()

print("Dzēstais elements:", removed)
print("Pēc pop:", numbers)

print("\n--- Slicing ---")

print("Pirmie 3 elementi:", numbers[:3])
print("Pēdējie 2 elementi:", numbers[-2:])

print("\n--- Cikls ---")

for number in numbers:
    print("Skaitlis:", number)
print("\n--- Enumerate ---")

for index, number in enumerate(numbers):
    print(index, "->", number)
print("\n--- List Comprehension ---")

squares = [number ** 2 for number in numbers]

print("Kvadrāti:", squares)
print("\n--- Dict ---")

student = {
    "name": "Olga",
    "age": 32,
    "course": "Python"
}

print(student)

print("Vārds:", student["name"])

student["age"] = 33

print("Jaunais vecums:", student["age"])
print("\n--- Studenti ---")

students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

print("Sākuma dati:", students)

# Pievieno studentu
students["Olga"] = 88

print("Pēc pievienošanas:", students)

# Maina atzīmi
students["Jānis"] = 80

print("Pēc atzīmes maiņas:", students)

print("\n--- Visi studenti ---")

for name, grade in students.items():
    print(name, "->", grade)
print("\n--- Labākā atzīme ---")

best_student = ""
best_grade = 0

for name, grade in students.items():

    if grade > best_grade:
        best_grade = grade
        best_student = name

print("Labākais students:", best_student)
print("Atzīme:", best_grade)
print("\n--- Studentu saraksts ---")

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 72},
    {"name": "Līga", "grade": 95},
    {"name": "Olga", "grade": 88}
]

print(student_list)
print("\n--- Filtrēšana ---")

for student in student_list:

    if student["grade"] >= 80:
        print(student)
print("\n--- Formatēta izvade ---")

for index, student in enumerate(student_list, start=1):

    print(f"{index}. {student['name']} — {student['grade']}")