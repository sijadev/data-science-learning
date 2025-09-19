# Python Installation und Setup Guide

## 🐍 Python Installation

### Windows

#### Option 1: Python.org (Empfohlen)
1. Gehe zu [python.org/downloads](https://python.org/downloads/)
2. Lade die neueste Python Version herunter
3. **Wichtig**: Aktiviere "Add Python to PATH" während der Installation
4. Wähle "Install Now" oder "Customize installation"
5. Verifiziere die Installation:
   ```cmd
   python --version
   pip --version
   ```

#### Option 2: Microsoft Store
1. Öffne Microsoft Store
2. Suche nach "Python"
3. Installiere Python 3.x
4. Automatisch zu PATH hinzugefügt

#### Option 3: Chocolatey
```powershell
# Chocolatey installieren (als Administrator)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Python installieren
choco install python
```

### macOS

#### Option 1: Python.org
1. Gehe zu [python.org/downloads](https://python.org/downloads/)
2. Lade den macOS Installer herunter
3. Führe die .pkg Datei aus
4. Verifiziere die Installation:
   ```bash
   python3 --version
   pip3 --version
   ```

#### Option 2: Homebrew (Empfohlen)
```bash
# Homebrew installieren
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python installieren
brew install python

# Alias setzen (optional)
echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc
source ~/.zshrc
```

#### Option 3: pyenv (für mehrere Python Versionen)
```bash
# pyenv installieren
brew install pyenv

# .zshrc konfigurieren
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Neustart oder source
source ~/.zshrc

# Python Version installieren
pyenv install 3.12.0
pyenv global 3.12.0
```

### Linux (Ubuntu/Debian)

#### Option 1: APT Package Manager
```bash
# System updaten
sudo apt update
sudo apt upgrade

# Python installieren
sudo apt install python3 python3-pip python3-venv

# Symlink erstellen (optional)
sudo ln -s /usr/bin/python3 /usr/bin/python
```

#### Option 2: Deadsnakes PPA (neueste Versionen)
```bash
# PPA hinzufügen
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Spezifische Python Version installieren
sudo apt install python3.12 python3.12-pip python3.12-venv
```

### Linux (CentOS/RHEL/Fedora)

```bash
# Fedora
sudo dnf install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip
# oder für neuere Versionen
sudo dnf install python3 python3-pip
```

## 🔧 Entwicklungsumgebung Setup

### Virtual Environment erstellen
```bash
# Virtual Environment erstellen
python -m venv myproject_env

# Aktivieren
# Windows:
myproject_env\Scripts\activate
# macOS/Linux:
source myproject_env/bin/activate

# Deaktivieren
deactivate
```

## 📝 VS Code Setup

### Installation

#### Windows
1. Gehe zu [code.visualstudio.com](https://code.visualstudio.com/)
2. Lade VS Code herunter
3. Installiere mit Standard-Einstellungen

#### macOS
```bash
# Homebrew
brew install --cask visual-studio-code

# Oder manuell von der Website
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64,arm64,armhf] https://packages.microsoft.com/repos/code stable main"
sudo apt update
sudo apt install code
```

### Python Extensions installieren

1. **Python Extension Pack** (ms-python.python)
   - Automatische Python Erkennung
   - IntelliSense
   - Debugging
   - Linting

2. **Pylance** (ms-python.vscode-pylance)
   - Erweiterte Typerkennung
   - Bessere Performance

3. **Python Docstring Generator** (njpwerner.autodocstring)
   - Automatische Docstring Generierung

4. **Black Formatter** (ms-python.black-formatter)
   - Code Formatierung

### VS Code Konfiguration

Erstelle `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./myproject_env/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "88"],
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

## 🚀 PyCharm Setup

### Installation

#### Windows
1. Gehe zu [jetbrains.com/pycharm](https://jetbrains.com/pycharm/)
2. Wähle Community (kostenlos) oder Professional
3. Lade herunter und installiere

#### macOS
```bash
# Homebrew
brew install --cask pycharm-ce
# oder für Professional
brew install --cask pycharm

# Oder manuell von der Website
```

#### Linux
```bash
# Snap
sudo snap install pycharm-community --classic
# oder für Professional
sudo snap install pycharm-professional --classic

# Oder Toolbox verwenden
```

### PyCharm Konfiguration

1. **Projekt erstellen**
   - File → New Project
   - Wähle Project Location
   - Konfiguriere Python Interpreter

2. **Interpreter Setup**
   - File → Settings → Project → Python Interpreter
   - Füge Virtual Environment hinzu
   - Oder verwende System Python

3. **Code Style konfigurieren**
   - File → Settings → Editor → Code Style → Python
   - Setze Line Length auf 88 (Black Standard)
   - Aktiviere Auto-Import

4. **Plugins installieren**
   - File → Settings → Plugins
   - Empfohlene Plugins:
     - Material Theme UI
     - Rainbow Brackets
     - GitToolBox

### PyCharm Shortcuts (wichtigste)

```
Ctrl+Shift+F10  : Datei ausführen
Ctrl+D          : Zeile duplizieren
Ctrl+Y          : Zeile löschen
Ctrl+/          : Kommentar toggle
Ctrl+Shift+F    : In Dateien suchen
Ctrl+R          : Ersetzen
Shift+F6        : Refactor/Rename
Ctrl+Alt+L      : Code formatieren
```

## 🔍 Zusätzliche Tools

### Package Manager Alternativen

#### Poetry (Empfohlen für Projekte)
```bash
# Installation
curl -sSL https://install.python-poetry.org | python3 -

# Projekt initialisieren
poetry init
poetry add requests
poetry install
```

#### Conda
```bash
# Miniconda installieren
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Environment erstellen
conda create -n myproject python=3.12
conda activate myproject
```

### Linting und Formatierung

```bash
# Installation
pip install black pylint flake8 mypy

# Verwendung
black .
pylint myfile.py
flake8 .
mypy myfile.py
```

## ✅ Installationsverifikation

Erstelle eine Test-Datei `test_installation.py`:

```python
import sys
import pip

def test_installation():
    print(f"Python Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    print(f"Pip Version: {pip.__version__}")

    try:
        import requests
        print("✅ Requests installiert")
    except ImportError:
        print("❌ Requests nicht gefunden - installiere mit: pip install requests")

    print("🎉 Python Installation erfolgreich!")

if __name__ == "__main__":
    test_installation()
```

Führe aus:
```bash
python test_installation.py
```

## 🛠️ Troubleshooting

### Häufige Probleme

1. **"Python nicht gefunden"**
   - PATH Variable prüfen
   - Python neu installieren mit "Add to PATH"

2. **Pip nicht verfügbar**
   ```bash
   python -m ensurepip --upgrade
   ```

3. **Permission Denied (Linux/macOS)**
   ```bash
   # Verwende --user flag
   pip install --user package_name
   ```

4. **Virtual Environment Probleme**
   ```bash
   # Environment löschen und neu erstellen
   rm -rf myproject_env
   python -m venv myproject_env
   ```

## 📚 Nächste Schritte

1. Erstelle dein erstes Python Projekt
2. Lerne über Package Management
3. Konfiguriere Git für Versionskontrolle
4. Erkunde Testing mit pytest
5. Lerne über Code Quality Tools