# Modul 1: Erste Schritte mit Python

## 1.1 Installation und Einrichtung

### Lernziele
- Python auf verschiedenen Betriebssystemen installieren
- Entwicklungsumgebung einrichten (VS Code/PyCharm)
- Erste Programme ausführen und testen

### Kernkonzepte

#### Python Installation
Python ist eine interpretierte Sprache, die einen Interpreter benötigt:
- **Windows**: Python.org Download oder Microsoft Store
- **macOS**: Homebrew oder Python.org
- **Linux**: Meist vorinstalliert oder über Package Manager

#### Virtual Environments
Isolierte Python-Umgebungen für Projekte:
```bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
```

#### Package Management mit pip
```bash
pip install package_name
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Praktische Übungen
1. Python installieren und Version prüfen
2. Virtual Environment erstellen und aktivieren
3. Ein Package installieren und importieren
4. "Hello World" Programm schreiben und ausführen

---

## 1.2 Grundlegende Syntax

### Lernziele
- Python-Philosophie und PEP 8 verstehen
- Mit der interaktiven Shell (REPL) arbeiten
- Code-Struktur und Einrückungen beherrschen
- Kommentare und Dokumentation schreiben

### Kernkonzepte

#### Python-Philosophie
```python
import this  # The Zen of Python
```
Wichtige Prinzipien:
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

#### REPL (Read-Eval-Print Loop)
Interaktive Python-Shell für schnelle Tests:
```python
>>> 2 + 2
4
>>> print("Hello")
Hello
>>> type(42)
<class 'int'>
```

#### Einrückung (Indentation)
Python verwendet Einrückung für Code-Blöcke:
```python
if condition:
    # 4 Leerzeichen Einrückung
    do_something()
    if nested_condition:
        # Weitere 4 Leerzeichen
        do_nested()
```

#### PEP 8 - Style Guide
- **Variablen**: `snake_case`
- **Konstanten**: `UPPER_CASE`
- **Klassen**: `PascalCase`
- **Private**: `_leading_underscore`
- Zeilenlänge: max. 79 Zeichen
- Imports am Dateianfang

#### Kommentare und Docstrings
```python
# Einzeiliger Kommentar

"""
Mehrzeiliger Kommentar
oder Docstring
"""

def function(param):
    """
    Funktionsbeschreibung.

    Args:
        param: Parameter-Beschreibung
    Returns:
        Rückgabewert-Beschreibung
    """
    pass
```

### Praktische Übungen
1. Python-Zen ausgeben und interpretieren
2. Mit der REPL experimentieren
3. Ein Programm mit korrekter Einrückung schreiben
4. PEP 8 konforme Variablennamen verwenden
5. Funktionen mit Docstrings dokumentieren

### Häufige Fehler und Lösungen

#### IndentationError
```python
# Falsch
if True:
print("Error")  # IndentationError

# Richtig
if True:
    print("OK")
```

#### Tab vs. Spaces
- Niemals Tabs und Spaces mischen!
- PEP 8 empfiehlt: 4 Spaces

### Best Practices
1. **Konsistente Einrückung**: Immer 4 Spaces verwenden
2. **Aussagekräftige Namen**: `user_age` statt `a`
3. **Kommentare sparsam**: Code sollte selbsterklärend sein
4. **Docstrings**: Für alle öffentlichen Funktionen/Klassen
5. **Leerzeilen**: Zur besseren Lesbarkeit nutzen

### Weiterführende Ressourcen
- [PEP 8 - Style Guide](https://pep8.org/)
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python - Python Basics](https://realpython.com/python-basics/)
- [Python Tutor - Visualize Code](https://pythontutor.com/)