# Funktionen definieren und aufrufen

# Einfache Funktion
print("=== Einfache Funktion ===")
def begrüßung():
    print("Hallo! Willkommen zu Python!")

begrüßung()

# Funktion mit Parameter
print("\n=== Funktion mit Parameter ===")
def persönliche_begrüßung(name):
    print(f"Hallo {name}! Schön dich zu sehen!")

persönliche_begrüßung("Alice")
persönliche_begrüßung("Bob")

# Funktion mit mehreren Parametern
print("\n=== Mehrere Parameter ===")
def addieren(a, b):
    ergebnis = a + b
    print(f"{a} + {b} = {ergebnis}")
    return ergebnis

summe = addieren(5, 3)
print(f"Rückgabewert: {summe}")

# Funktion mit Standardwerten
print("\n=== Standardwerte ===")
def begrüßung_mit_zeit(name, tageszeit="Tag"):
    print(f"Guten {tageszeit}, {name}!")

begrüßung_mit_zeit("Charlie")
begrüßung_mit_zeit("Diana", "Morgen")
begrüßung_mit_zeit("Eve", "Abend")

# Benannte Argumente (Keyword Arguments)
print("\n=== Benannte Argumente ===")
def person_vorstellen(name, alter, beruf="Student"):
    print(f"Das ist {name}, {alter} Jahre alt, arbeitet als {beruf}")

person_vorstellen("Franz", 25)
person_vorstellen(name="Greta", beruf="Ärztin", alter=30)
person_vorstellen(alter=22, name="Hans")

# Variable Anzahl von Argumenten
print("\n=== Variable Argumente (*args) ===")
def alle_addieren(*zahlen):
    summe = 0
    for zahl in zahlen:
        summe += zahl
    print(f"Summe von {zahlen} = {summe}")
    return summe

alle_addieren(1, 2, 3)
alle_addieren(5, 10, 15, 20)
alle_addieren(100)

# Variable Keyword-Argumente
print("\n=== Variable Keyword-Argumente (**kwargs) ===")
def person_info(**info):
    print("Person-Informationen:")
    for schlüssel, wert in info.items():
        print(f"  {schlüssel}: {wert}")

person_info(name="Ida", alter=28, beruf="Lehrerin")
person_info(name="Jan", stadt="München", hobby="Fußball", alter=35)

# Kombinierte Parameter
print("\n=== Kombinierte Parameter ===")
def vollständige_funktion(pflicht_arg, standard_arg="Standard", *args, **kwargs):
    print(f"Pflicht-Argument: {pflicht_arg}")
    print(f"Standard-Argument: {standard_arg}")
    print(f"Zusätzliche Argumente: {args}")
    print(f"Keyword-Argumente: {kwargs}")

vollständige_funktion("Wichtig", "Geändert", 1, 2, 3, name="Klaus", alter=40)

# Lokale vs. Globale Variablen
print("\n=== Lokale vs. Globale Variablen ===")
globale_variable = "Ich bin global"

def variable_test():
    lokale_variable = "Ich bin lokal"
    print(f"In Funktion - Global: {globale_variable}")
    print(f"In Funktion - Lokal: {lokale_variable}")

variable_test()
print(f"Außerhalb - Global: {globale_variable}")
# print(lokale_variable)  # Das würde einen Fehler verursachen!

# Global-Keyword
print("\n=== Global-Keyword ===")
zähler = 0

def zähler_erhöhen():
    global zähler
    zähler += 1
    print(f"Zähler in Funktion: {zähler}")

print(f"Zähler vorher: {zähler}")
zähler_erhöhen()
zähler_erhöhen()
print(f"Zähler nachher: {zähler}")

# Funktionen als Rückgabewerte
print("\n=== Funktionen als Rückgabewerte ===")
def rechner_erstellen(operation):
    if operation == "add":
        def addieren(a, b):
            return a + b
        return addieren
    elif operation == "mult":
        def multiplizieren(a, b):
            return a * b
        return multiplizieren

addierer = rechner_erstellen("add")
multiplizierer = rechner_erstellen("mult")

print(f"5 + 3 = {addierer(5, 3)}")
print(f"4 * 6 = {multiplizierer(4, 6)}")

# Lambda-Funktionen (kurze anonyme Funktionen)
print("\n=== Lambda-Funktionen ===")
quadrat = lambda x: x ** 2
print(f"5² = {quadrat(5)}")

summe_lambda = lambda a, b: a + b
print(f"7 + 8 = {summe_lambda(7, 8)}")

# Lambda mit Listen
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x**2, zahlen))
print(f"Quadrate: {quadrate}")

gerade = list(filter(lambda x: x % 2 == 0, zahlen))
print(f"Gerade Zahlen: {gerade}")