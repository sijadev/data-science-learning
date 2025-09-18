#!/usr/bin/env python3
"""
Tag 1: Python Basics - Variablen und Datentypen
Verbindung zu Testing: Test-Daten verstehen
Vorbereitung für das eigentliche Projekt Testmanager
"""

# 1. Variablen & Typen (wie Test-Daten)
test_name = "Login_Test_001"
test_passed = True
execution_time = 2.34
error_count = 0
test_tags = ["smoke", "regession", "critical"]


# Test date output
print(f"Test: {test_name}")
print(f"Status: {'Passed' if test_passed else 'Failed'}")
print(f"Execution: {execution_time} s")

# 2. Dictionary as Test Result
test_result = {
    "test_id": "TC_001",
    "description": "Verify user logoin with valid credentials",
    "status": "passed",
    "duration": 2.34,
    "timestamp": "2025-01-15 10:30:00",
    "enviroment": "staging"
}

# Test Result output
import json
print("")