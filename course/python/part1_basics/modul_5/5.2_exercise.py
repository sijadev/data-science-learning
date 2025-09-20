# Scope und Namespaces
# Übung: Variable Sichtbarkeit

# TODO: Global vs Local
globale_variable = "Ich bin global"

def lokale_funktion():
    lokale_variable = "Ich bin lokal"
    print(f"In Funktion: {lokale_variable}")
    print(f"Global zugänglich: {globale_variable}")

lokale_funktion()
print(f"Außerhalb: {globale_variable}")

# TODO: Global Keyword
zähler = 0

def erhöhe_zähler():
    global zähler
    zähler += 1
    print(f"Zähler: {zähler}")

erhöhe_zähler()
erhöhe_zähler()

# TODO: Closures
def erstelle_multiplikator(faktor):
    def multiplikator(zahl):
        return zahl * faktor
    return multiplikator

verdoppeln = erstelle_multiplikator(2)
verdreifachen = erstelle_multiplikator(3)

print(f"5 * 2 = {verdoppeln(5)}")
print(f"5 * 3 = {verdreifachen(5)}")

# TODO: nonlocal
def erstelle_zähler():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

mein_zähler = erstelle_zähler()
print(f"Zähler: {mein_zähler()}")
print(f"Zähler: {mein_zähler()}")
print(f"Zähler: {mein_zähler()}")