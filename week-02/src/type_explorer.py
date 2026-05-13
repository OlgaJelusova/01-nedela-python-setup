# === MAINĪGIE AR DAŽĀDIEM TIPIEM ===

teksts = "Sveika!"
skaitlis = 10
decimals = 3.14
patiesiba = True
nekas = None

# === IZVADĪT TIPUS ===

print("teksts tips:", type(teksts))
print("skaitlis tips:", type(skaitlis))
print("decimals tips:", type(decimals))
print("patiesiba tips:", type(patiesiba))
print("nekas tips:", type(nekas))


# === TRUTHY / FALSY PIEMĒRI ===

print(bool(""))        # False (tukša virkne)
print(bool(" "))       # True (ir simbols!)
print(bool(0))         # False
print(bool(1))         # True
print(bool([]))        # False
print(bool(None))      # False


# === DATU TIPU PĀRVEIDOŠANA ===

print(int("5") + 3)        # 8
print(float("3.14"))       # 3.14
print(str(100) + " euro")  # "100 euro"

# Kļūdas piemērs (nepalaid šo rindu bez komentāra)
# print(int("abc"))        # ValueError!


# === INTERESANTI PIEMĒRI ===

print(True + True)     # 2
print(True * 10)       # 10
print(0.1 + 0.2 == 0.3)  # False