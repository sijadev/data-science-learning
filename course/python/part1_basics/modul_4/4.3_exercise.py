# Dictionaries
# Übung: Schlüssel-Wert Paare

# TODO: Dictionary erstellen
person = {
    "name": "Alice",
    "alter": 30,
    "stadt": "Berlin",
    "beruf": "Entwicklerin"
}

# TODO: Zugriff und Manipulation
print(f"Name: {person['name']}")
print(f"Alter: {person.get('alter', 'Unbekannt')}")

person["alter"] = 31  # Ändern
person["email"] = "alice@example.com"  # Hinzufügen
print(f"Aktualisiert: {person}")

# TODO: Dictionary Methoden
print(f"Schlüssel: {list(person.keys())}")
print(f"Werte: {list(person.values())}")
print(f"Paare: {list(person.items())}")

# TODO: Dictionary Comprehension
quadrate = {x: x**2 for x in range(1, 6)}
print(f"Quadrate: {quadrate}")

# TODO: Verschachtelte Dictionaries
adressbuch = {
    "Alice": {"telefon": "123", "email": "alice@test.de"},
    "Bob": {"telefon": "456", "email": "bob@test.de"}
}
print(f"Alice's Email: {adressbuch['Alice']['email']}")