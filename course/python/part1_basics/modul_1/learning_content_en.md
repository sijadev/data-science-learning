# Module 1: Getting Started with Python

## 1.1 Installation and Setup

### Learning Objectives
- Install Python on different operating systems
- Set up development environment (VS Code/PyCharm)
- Run and test first programs

### Core Concepts

#### Python Installation
Python is an interpreted language that requires an interpreter:
- **Windows**: Python.org download or Microsoft Store
- **macOS**: Homebrew or Python.org
- **Linux**: Usually pre-installed or via package manager

#### Virtual Environments
Isolated Python environments for projects:
```bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
```

#### Package Management with pip
```bash
pip install package_name
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Practical Exercises
1. Install Python and check version
2. Create and activate virtual environment
3. Install a package and import it
4. Write and run "Hello World" program

---

## 1.2 Basic Syntax

### Learning Objectives
- Understand Python philosophy and PEP 8
- Work with the interactive shell (REPL)
- Master code structure and indentation
- Write comments and documentation

### Core Concepts

#### Python Philosophy
```python
import this  # The Zen of Python
```
Important principles:
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

#### REPL (Read-Eval-Print Loop)
Interactive Python shell for quick tests:
```python
>>> 2 + 2
4
>>> print("Hello")
Hello
>>> type(42)
<class 'int'>
```

#### Indentation
Python uses indentation for code blocks:
```python
if condition:
    # 4 spaces indentation
    do_something()
    if nested_condition:
        # Another 4 spaces
        do_nested()
```

#### PEP 8 - Style Guide
- **Variables**: `snake_case`
- **Constants**: `UPPER_CASE`
- **Classes**: `PascalCase`
- **Private**: `_leading_underscore`
- Line length: max. 79 characters
- Imports at top of file

#### Comments and Docstrings
```python
# Single-line comment

"""
Multi-line comment
or docstring
"""

def function(param):
    """
    Function description.

    Args:
        param: Parameter description
    Returns:
        Return value description
    """
    pass
```

### Practical Exercises
1. Display Python Zen and interpret it
2. Experiment with the REPL
3. Write a program with correct indentation
4. Use PEP 8 compliant variable names
5. Document functions with docstrings

### Common Errors and Solutions

#### IndentationError
```python
# Wrong
if True:
print("Error")  # IndentationError

# Correct
if True:
    print("OK")
```

#### Tab vs. Spaces
- Never mix tabs and spaces!
- PEP 8 recommends: 4 spaces

### Best Practices
1. **Consistent indentation**: Always use 4 spaces
2. **Meaningful names**: `user_age` instead of `a`
3. **Sparse comments**: Code should be self-explanatory
4. **Docstrings**: For all public functions/classes
5. **Blank lines**: Use for better readability

### Further Resources
- [PEP 8 - Style Guide](https://pep8.org/)
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python - Python Basics](https://realpython.com/python-basics/)
- [Python Tutor - Visualize Code](https://pythontutor.com/)