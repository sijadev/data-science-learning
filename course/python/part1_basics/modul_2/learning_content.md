# Modul 2: Datentypen und Variablen

## 2.1 Basis-Datentypen

### Lernziele
- Die grundlegenden Datentypen in Python verstehen
- Type Casting und Typkonvertierung durchführen
- Mit verschiedenen Zahlenformaten arbeiten
- String-Operationen beherrschen

### Kernkonzepte

#### Numerische Typen

##### Integer (int)
Ganze Zahlen ohne Dezimalpunkt:
```python
age = 25
negative = -42
binary = 0b1010     # 10 in Dezimal
hexadecimal = 0xFF  # 255 in Dezimal
million = 1_000_000 # Unterstriche für Lesbarkeit
```

##### Float
Gleitkommazahlen mit Dezimalpunkt:
```python
pi = 3.14159
temperature = -17.5
scientific = 2.5e-3  # 0.0025
```
**Achtung**: Floating-Point Arithmetik ist nicht exakt!
```python
0.1 + 0.2 == 0.3  # False!
```

##### Complex
Komplexe Zahlen mit Real- und Imaginärteil:
```python
z = 3 + 4j
z.real    # 3.0
z.imag    # 4.0
abs(z)    # 5.0 (Betrag)
```

#### String (str)
Zeichenketten für Text:
```python
single = 'Einfache Anführungszeichen'
double = "Doppelte Anführungszeichen"
triple = """Mehrzeilige
Zeichenkette"""
raw = r"Raw String: \n wird nicht interpretiert"
```

**String-Operationen**:
- Indizierung: `text[0]` (erstes Zeichen)
- Slicing: `text[1:5]` (Substring)
- Konkatenation: `"Hello" + " " + "World"`
- Wiederholung: `"Ha" * 3` → "HaHaHa"
- Methoden: `.upper()`, `.lower()`, `.strip()`, `.split()`

#### Boolean (bool)
Wahrheitswerte True und False:
```python
is_active = True
is_deleted = False
```

**Falsy Werte** (werden als False interpretiert):
- `0`, `0.0`, `0j`
- `""` (leerer String)
- `[]`, `()`, `{}` (leere Container)
- `None`

**Truthy Werte**: Alle anderen Werte

#### None
Repräsentiert "kein Wert" oder "nicht definiert":
```python
result = None
if result is None:  # Best Practice: 'is' verwenden
    print("Kein Ergebnis")
```

#### Type Casting
Explizite Typkonvertierung:
```python
int("42")      # String zu Integer
float("3.14")  # String zu Float
str(100)       # Zahl zu String
bool(1)        # Zahl zu Boolean
list("abc")    # String zu Liste ['a', 'b', 'c']
```

### Praktische Übungen
1. Verschiedene Zahlenformate erstellen und konvertieren
2. String-Manipulationen durchführen
3. Type Casting mit Fehlerbehandlung
4. Truthy/Falsy Werte testen

---

## 2.2 Variablen und Operatoren

### Lernziele
- Variablenzuweisung und Namenskonventionen verstehen
- Alle Operatortypen beherrschen
- Operator-Priorität verstehen
- Ausdrücke korrekt auswerten

### Kernkonzepte

#### Variablenzuweisung
```python
# Einfache Zuweisung
name = "Python"

# Mehrfachzuweisung
x, y, z = 1, 2, 3

# Gleiche Werte
a = b = c = 0

# Tuple Unpacking
coordinates = (10, 20)
x, y = coordinates

# Variablen tauschen
x, y = y, x
```

#### Arithmetische Operatoren
| Operator | Beschreibung | Beispiel | Ergebnis |
|----------|--------------|----------|----------|
| + | Addition | 10 + 3 | 13 |
| - | Subtraktion | 10 - 3 | 7 |
| * | Multiplikation | 10 * 3 | 30 |
| / | Division | 10 / 3 | 3.333... |
| // | Ganzzahldivision | 10 // 3 | 3 |
| % | Modulo (Rest) | 10 % 3 | 1 |
| ** | Potenz | 2 ** 3 | 8 |

#### Vergleichsoperatoren
```python
==  # Gleich
!=  # Ungleich
>   # Größer
<   # Kleiner
>=  # Größer oder gleich
<=  # Kleiner oder gleich
```

**Verkettete Vergleiche**:
```python
1 < x < 10  # Äquivalent zu: 1 < x and x < 10
```

#### Logische Operatoren
```python
and  # Logisches UND
or   # Logisches ODER
not  # Logische Verneinung
```

**Short-Circuit Evaluation**:
- `and` stoppt bei erstem False
- `or` stoppt bei erstem True

#### Bitweise Operatoren
```python
&   # Bitweises AND
|   # Bitweises OR
^   # Bitweises XOR
~   # Bitweise NOT
<<  # Left Shift
>>  # Right Shift
```

#### Zuweisungsoperatoren
```python
+=   # x += 5  → x = x + 5
-=   # x -= 3  → x = x - 3
*=   # x *= 2  → x = x * 2
/=   # x /= 2  → x = x / 2
//=  # x //= 2 → x = x // 2
%=   # x %= 3  → x = x % 3
**=  # x **= 2 → x = x ** 2
```

#### Identitäts- und Mitgliedschaftsoperatoren
```python
# Identität (vergleicht Objekt-IDs)
is      # x is y
is not  # x is not y

# Mitgliedschaft
in      # x in sequence
not in  # x not in sequence
```

#### Walrus Operator := (Python 3.8+)
Zuweisung in Ausdrücken:
```python
if (n := len(data)) > 10:
    print(f"Liste hat {n} Elemente")
```

### Operator-Priorität
Von höchster zu niedrigster:
1. `()` Klammern
2. `**` Potenz
3. `+x`, `-x`, `~x` Unäre Operatoren
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `<`, `<=`, `>`, `>=`
11. `is`, `is not`, `in`, `not in`
12. `not`
13. `and`
14. `or`

### Best Practices
1. **Aussagekräftige Variablennamen**: `user_age` statt `a`
2. **Konstanten in GROSSBUCHSTABEN**: `MAX_SIZE = 100`
3. **Spaces um Operatoren**: `x = y + z` nicht `x=y+z`
4. **Klammern für Klarheit**: `(a + b) * c` wenn unsicher
5. **`is` für None-Vergleich**: `if x is None:` nicht `if x == None:`

### Häufige Fehler und Lösungen

#### Integer Division
```python
# Fehler: Unerwartetes Ergebnis
result = 5 / 2  # 2.5 (float)

# Lösung: Ganzzahldivision verwenden
result = 5 // 2  # 2 (int)
```

#### Mutable Default-Argumente
```python
# Fehler
def add_item(item, liste=[]):  # Gefährlich!
    liste.append(item)
    return liste

# Lösung
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

### Praktische Übungen
1. Taschenrechner mit allen arithmetischen Operationen
2. Bit-Flags für Berechtigungen implementieren
3. Ausdrücke mit verschiedenen Operatorprioritäten auswerten
4. Short-Circuit Evaluation demonstrieren

### Weiterführende Ressourcen
- [Python Operators Documentation](https://docs.python.org/3/library/operator.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python - Operators and Expressions](https://realpython.com/python-operators-expressions/)