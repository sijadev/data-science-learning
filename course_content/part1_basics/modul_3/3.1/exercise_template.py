# Bedingte Anweisungen
# Übung: if, elif, else

# TODO: Einfache if-Anweisung
alter = 18
if alter >= 18:
    print("Du bist volljährig!")

# TODO: if-elif-else Kette
note = 85
if note >= 90:
    print("Ausgezeichnet!")
elif note >= 80:
    print("Sehr gut!")
elif note >= 70:
    print("Gut!")
else:
    print("Kann verbessert werden")

# TODO: Ternärer Operator
status = "aktiv" if alter >= 18 else "inaktiv"
print(f"Status: {status}")

# TODO: Verschachtelte Bedingungen
wetter = "sonnig"
temperatur = 25

if wetter == "sonnig":
    if temperatur > 20:
        print("Perfektes Wetter für draußen!")
    else:
        print("Sonnig aber kühl")

# TODO: match-case (Python 3.10+)
tag = "montag"
match tag:
    case "montag":
        print("Wochenstart!")
    case "freitag":
        print("Fast Wochenende!")
    case _:
        print("Ein normaler Tag")