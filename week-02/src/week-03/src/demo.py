from utils import average, factorial
from validators import (
    is_email,
    is_phone_number,
    is_valid_age
)

print("--- Utils ---")

print(average([1, 2, 3, 4]))
print(factorial(5))

print("\n--- Validators ---")

print(is_email("anna@gmail.com"))
print(is_phone_number("+371 26123456"))
print(is_valid_age(25))