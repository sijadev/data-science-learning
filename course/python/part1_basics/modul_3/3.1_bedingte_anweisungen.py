# 3.1 Bedingte Anweisungen - Code Examples

# ========================================
# If-Statement
# ========================================
print("=" * 50)
print("IF-STATEMENT")
print("=" * 50)

# Einfaches if
alter = 18
if alter >= 18:
    print("Du bist volljährig")

# if-else
temperatur = 25
if temperatur > 30:
    print("Es ist heiß")
else:
    print("Es ist angenehm")

# if-elif-else
note = 85
if note >= 90:
    print("Note: A")
elif note >= 80:
    print("Note: B")
elif note >= 70:
    print("Note: C")
elif note >= 60:
    print("Note: D")
else:
    print("Note: F")

# ========================================
# Verschachtelte Bedingungen
# ========================================
print("\n" + "=" * 50)
print("VERSCHACHTELTE BEDINGUNGEN")
print("=" * 50)

alter = 25
hat_fuehrerschein = True
nuechtern = True

if alter >= 18:
    if hat_fuehrerschein:
        if nuechtern:
            print("Du darfst fahren")
        else:
            print("Du darfst nicht fahren - nicht nüchtern!")
    else:
        print("Du darfst nicht fahren - kein Führerschein!")
else:
    print("Du darfst nicht fahren - zu jung!")

# Besser mit logischen Operatoren
if alter >= 18 and hat_fuehrerschein and nuechtern:
    print("\nAlternative: Du darfst fahren")
else:
    print("\nAlternative: Du darfst nicht fahren")

# ========================================
# Ternärer Operator (Conditional Expression)
# ========================================
print("\n" + "=" * 50)
print("TERNÄRER OPERATOR")
print("=" * 50)

# Syntax: value_if_true if condition else value_if_false
alter = 20
status = "volljährig" if alter >= 18 else "minderjährig"
print(f"Status: {status}")

# Mit Berechnung
x = 10
y = 20
maximum = x if x > y else y
print(f"Maximum von {x} und {y}: {maximum}")

# Verschachtelt (nicht empfohlen - schwer lesbar!)
note = 75
bewertung = "gut" if note >= 80 else ("befriedigend" if note >= 60 else "ungenügend")
print(f"Bewertung: {bewertung}")

# ========================================
# Match-Case (Python 3.10+)
# ========================================
print("\n" + "=" * 50)
print("MATCH-CASE (Pattern Matching)")
print("=" * 50)

# Einfaches Match
tag = "Montag"
match tag:
    case "Montag":
        print("Start der Woche")
    case "Freitag":
        print("Fast Wochenende!")
    case "Samstag" | "Sonntag":
        print("Wochenende!")
    case _:
        print("Normaler Wochentag")

# Mit Werten
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(f"\nHTTP 200: {http_status(200)}")
print(f"HTTP 404: {http_status(404)}")

# Mit Patterns und Guards
def kategorisiere_zahl(x):
    match x:
        case 0:
            return "Null"
        case n if n > 0:
            return "Positiv"
        case n if n < 0:
            return "Negativ"

print(f"\nKategorisiere 42: {kategorisiere_zahl(42)}")
print(f"Kategorisiere -5: {kategorisiere_zahl(-5)}")
print(f"Kategorisiere 0: {kategorisiere_zahl(0)}")

# Mit Strukturen
def verarbeite_punkt(punkt):
    match punkt:
        case (0, 0):
            return "Ursprung"
        case (0, y):
            return f"Auf Y-Achse bei y={y}"
        case (x, 0):
            return f"Auf X-Achse bei x={x}"
        case (x, y):
            return f"Punkt bei ({x}, {y})"

print(f"\n(0, 0): {verarbeite_punkt((0, 0))}")
print(f"(0, 5): {verarbeite_punkt((0, 5))}")
print(f"(3, 4): {verarbeite_punkt((3, 4))}")

# Mit Klassen/Typen
def verarbeite_daten(data):
    match data:
        case str(s):
            return f"String mit {len(s)} Zeichen"
        case int(n) if n > 0:
            return f"Positive Zahl: {n}"
        case list(l):
            return f"Liste mit {len(l)} Elementen"
        case dict(d):
            return f"Dictionary mit {len(d)} Keys"
        case _:
            return "Unbekannter Typ"

print(f"\n'Hallo': {verarbeite_daten('Hallo')}")
print(f"42: {verarbeite_daten(42)}")
print(f"[1,2,3]: {verarbeite_daten([1,2,3])}")
print(f"dict: {verarbeite_daten({'a': 1})}")

# ========================================
# Truthy und Falsy in Bedingungen
# ========================================
print("\n" + "=" * 50)
print("TRUTHY UND FALSY")
print("=" * 50)

# Falsy Werte
falsy_werte = [0, 0.0, "", [], (), {}, None, False]
for wert in falsy_werte:
    if not wert:
        print(f"{repr(wert):10} ist Falsy")

# Truthy Werte
print("\nTruthy Beispiele:")
if 42:
    print("42 ist Truthy")
if "Text":
    print("'Text' ist Truthy")
if [1, 2, 3]:
    print("[1, 2, 3] ist Truthy")

# ========================================
# Praktische Beispiele
# ========================================
print("\n" + "=" * 50)
print("PRAKTISCHE BEISPIELE")
print("=" * 50)

# Benutzer-Authentifizierung
def login(username, password):
    users = {"admin": "secret123", "user": "pass456"}

    if not username or not password:
        return "Bitte Username und Passwort eingeben"

    if username not in users:
        return "Benutzer nicht gefunden"

    if users[username] != password:
        return "Falsches Passwort"

    return f"Willkommen {username}!"

print(login("admin", "secret123"))
print(login("admin", "falsch"))
print(login("", ""))

# Schaltjahr-Prüfung
def ist_schaltjahr(jahr):
    if jahr % 400 == 0:
        return True
    elif jahr % 100 == 0:
        return False
    elif jahr % 4 == 0:
        return True
    else:
        return False

jahre = [1900, 2000, 2020, 2021, 2024]
print("\nSchaltjahr-Test:")
for jahr in jahre:
    print(f"{jahr}: {'Schaltjahr' if ist_schaltjahr(jahr) else 'Kein Schaltjahr'}")

# Rabatt-Berechnung
def berechne_rabatt(betrag, kunde_typ):
    if kunde_typ == "premium":
        if betrag > 100:
            return betrag * 0.8  # 20% Rabatt
        else:
            return betrag * 0.9  # 10% Rabatt
    elif kunde_typ == "regular":
        if betrag > 200:
            return betrag * 0.95  # 5% Rabatt
        else:
            return betrag
    else:
        return betrag

print("\nRabatt-Berechnung:")
print(f"Premium, 150€: {berechne_rabatt(150, 'premium'):.2f}€")
print(f"Regular, 250€: {berechne_rabatt(250, 'regular'):.2f}€")

# ========================================
# Erweiterte Techniken
# ========================================
print("\n" + "=" * 50)
print("ERWEITERTE TECHNIKEN")
print("=" * 50)

# Chained Comparisons
alter = 25
if 18 <= alter < 65:
    print("Im erwerbsfähigen Alter")

# Multiple Conditions mit any() und all()
bedingungen = [alter >= 18, hat_fuehrerschein, nuechtern]
if all(bedingungen):
    print("Alle Bedingungen erfüllt")

werte = [0, 1, 2, 3]
if any(werte):
    print("Mindestens ein Truthy-Wert")

# Dictionary als Switch-Ersatz (vor Python 3.10)
def operation(op, a, b):
    operationen = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Division durch Null!"
    }
    return operationen.get(op, "Unbekannte Operation")

print(f"\n5 + 3 = {operation('+', 5, 3)}")
print(f"5 / 0 = {operation('/', 5, 0)}")