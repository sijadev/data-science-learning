# Datentypen
# Übung: Arbeiten mit verschiedenen Datentypen

# TODO: Erstelle Variablen mit verschiedenen Datentypen
ganze_zahl = 42
komma_zahl = 3.14
text = "Python ist toll!"
wahrheitswert = True

# TODO: Konvertiere zwischen Datentypen
zahl_als_text = str(ganze_zahl)
text_als_zahl = int("100")
print(f"Konvertierung: {type(zahl_als_text)}, {type(text_als_zahl)}")

# TODO: Arbeite mit komplexen Zahlen
komplex = 3 + 4j
print(f"Komplexe Zahl: {komplex}")
print(f"Realteil: {komplex.real}, Imaginärteil: {komplex.imag}")

# TODO: Teste truthy und falsy Werte
falsy_werte = [None, False, 0, 0.0, "", [], {}, set()]
for wert in falsy_werte:
    if not wert:
        print(f"{wert} ist falsy")