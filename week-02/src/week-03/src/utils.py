def capitalize(text):
    """
    Pārvērš pirmo burtu lielajā.
    """

    return text.capitalize()


print(capitalize("hello"))

def truncate(text, max_len=20):
    """
    Saīsina tekstu un pievieno ...
    """

    if len(text) > max_len:
        return text[:max_len] + "..."

    return text


print(truncate("Python ir ļoti interesanta valoda", 10))

def count_words(text):
    """
    Saskaita vārdu skaitu tekstā.
    """

    words = text.split()

    return len(words)


print(count_words("Python ir ļoti interesants"))

def clamp(num, low, high):
    """
    Ierobežo skaitli diapazonā.
    """

    if num < low:
        return low

    elif num > high:
        return high

    return num


print(clamp(-5, 0, 10))
print(clamp(7, 0, 10))
print(clamp(20, 0, 10))

def is_prime(num):
    """
    Pārbauda vai skaitlis ir pirmskaitlis.
    """

    if num < 2:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


print(is_prime(2))
print(is_prime(4))
print(is_prime(7))

def factorial(n):
    """
    Aprēķina skaitļa faktoriālu.
    """

    if n < 0:
        return "Nederīgs skaitlis"

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))
print(factorial(3))

def total(numbers):
    """
    Aprēķina saraksta summu.
    """

    result = 0

    for number in numbers:
        result += number

    return result


print(total([1, 2, 3, 4]))

def average(numbers):
    """
    Aprēķina vidējo aritmētisko.
    """

    if len(numbers) == 0:
        return 0

    total_sum = total(numbers)

    return total_sum / len(numbers)


print(average([2, 4, 6]))