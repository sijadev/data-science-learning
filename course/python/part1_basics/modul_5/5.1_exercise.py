# Funktionen
# Übung: Funktionen definieren und verwenden

# TODO: Einfache Funktion
def begrüßung(name):
    """Begrüßt eine Person"""
    return f"Hallo, {name}!"

print(begrüßung("Alice"))

# TODO: Funktion mit mehreren Parametern
def berechne_rechteck(länge, breite):
    """Berechnet Fläche und Umfang eines Rechtecks"""
    fläche = länge * breite
    umfang = 2 * (länge + breite)
    return fläche, umfang

f, u = berechne_rechteck(5, 3)
print(f"Fläche: {f}, Umfang: {u}")

# TODO: Default Parameter
def potenz(basis, exponent=2):
    """Berechnet Potenz mit Default-Exponent 2"""
    return basis ** exponent

print(f"3^2 = {potenz(3)}")
print(f"3^3 = {potenz(3, 3)}")

# TODO: *args und **kwargs
def flexible_funktion(*args, **kwargs):
    """Flexibel Parameter"""
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_funktion(1, 2, 3, name="Alice", alter=30)

# TODO: Type Hints
def addiere(a: int, b: int) -> int:
    """Addiert zwei Zahlen mit Type Hints"""
    return a + b

print(f"2 + 3 = {addiere(2, 3)}")