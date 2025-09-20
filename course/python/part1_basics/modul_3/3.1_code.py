# Bedingte Anweisungen

# Einfache if-Anweisung
alter = 18
print("=== Einfache if-Anweisung ===")
if alter >= 18:
    print(f"Du bist {alter} Jahre alt und volljährig!")
else:
    print(f"Du bist {alter} Jahre alt und minderjährig.")

# if-elif-else Kette
print("\n=== Notenbewertung ===")
note = 85
if note >= 90:
    bewertung = "Ausgezeichnet!"
elif note >= 80:
    bewertung = "Sehr gut!"
elif note >= 70:
    bewertung = "Gut!"
elif note >= 60:
    bewertung = "Befriedigend"
else:
    bewertung = "Nicht bestanden"

print(f"Note {note}: {bewertung}")

# Ternärer Operator
print("\n=== Ternärer Operator ===")
status = "aktiv" if alter >= 18 else "inaktiv"
print(f"Account Status: {status}")

# Verschachtelte Bedingungen
print("\n=== Wetter-Check ===")
wetter = "sonnig"
temperatur = 25

if wetter == "sonnig":
    if temperatur > 20:
        aktivität = "Perfekt für Outdoor-Aktivitäten!"
    else:
        aktivität = "Sonnig aber kühl - Jacke mitnehmen!"
elif wetter == "regnerisch":
    aktivität = "Besser drinnen bleiben"
else:
    aktivität = "Wetter prüfen"

print(f"Bei {temperatur}°C und {wetter}em Wetter: {aktivität}")

# match-case (Python 3.10+)
print("\n=== Wochentag-Info ===")
tag = "montag"
match tag.lower():
    case "montag":
        info = "Wochenstart - frisch ans Werk!"
    case "mittwoch":
        info = "Mitte der Woche - durchhalten!"
    case "freitag":
        info = "Fast geschafft - Wochenende naht!"
    case "samstag" | "sonntag":
        info = "Wochenende - Zeit zum Entspannen!"
    case _:
        info = "Ein ganz normaler Tag"

print(f"{tag.capitalize()}: {info}")
