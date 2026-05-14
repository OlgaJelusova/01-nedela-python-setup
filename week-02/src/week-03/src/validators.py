def is_email(text):
    """
    Pārbauda vai teksts ir e-pasts.
    """

    return "@" in text and "." in text


print(is_email("anna@gmail.com"))
print(is_email("hello"))
print(is_email("anna@"))

def is_phone_number(text):
    """
    Pārbauda Latvijas telefona numuru formātā +371 XXXXXXXX.
    """

    if not text.startswith("+371 "):
        return False

    number = text[5:]

    return number.isdigit() and len(number) == 8
print(is_phone_number("+371 26123456"))
print(is_phone_number("26123456"))
print(is_phone_number("+371 123"))
print(is_phone_number("+371 abcdefgh"))

def is_valid_age(age):
    """
    Pārbauda vai vecums ir derīgs.
    """

    return isinstance(age, int) and 0 <= age <= 150


print(is_valid_age(25))
print(is_valid_age(200))
print(is_valid_age(-5))
print(is_valid_age("20"))


def is_strong_password(text):
    """
    Pārbauda vai parole ir droša.
    """

    has_letter = False
    has_digit = False

    for char in text:

        if char.isalpha():
            has_letter = True

        if char.isdigit():
            has_digit = True

    return len(text) >= 8 and has_letter and has_digit


print(is_strong_password("abc123"))
print(is_strong_password("mypassword1"))
print(is_strong_password("12345678"))
print(is_strong_password("password"))

def is_valid_date(text):
    """
    Pārbauda datuma formātu YYYY-MM-DD.
    """

    parts = text.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    return (
    year.isdigit()
    and month.isdigit()
    and day.isdigit()
    and len(year) == 4
    and len(month) == 2
    and len(day) == 2
)


print(is_valid_date("2025-05-14"))
print(is_valid_date("14-05-2025"))
print(is_valid_date("hello"))
