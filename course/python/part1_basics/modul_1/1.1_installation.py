# 1.1 Installation and Setup - Code Examples

# Python Installation Test
print("Hello World!")
print("Python is successfully installed!")

# Show version
import sys
print(f"Python Version: {sys.version}")
print(f"Python Executable: {sys.executable}")

# Check pip version
try:
    import pip
    print(f"Pip Version: {pip.__version__}")
except ImportError:
    print("Pip not found")

# Check virtual environment
import os
in_venv = hasattr(sys, 'real_prefix') or (
    hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
)
print(f"In virtual environment: {in_venv}")

# Test important modules
modules_to_test = ['os', 'math', 'random', 'datetime', 'json']
print("\n📦 Standard Module Check:")
for module in modules_to_test:
    try:
        __import__(module)
        print(f"✅ {module} - available")
    except ImportError:
        print(f"❌ {module} - not found")

# Platform Information
import platform
print(f"\n💻 System Information:")
print(f"OS: {platform.system()} {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print(f"Python Build: {platform.python_build()}")