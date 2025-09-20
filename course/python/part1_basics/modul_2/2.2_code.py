# Variablen und Operatoren

# Arithmetische Operatoren
a = 15
b = 4

print("=== Arithmetische Operatoren ===")
print(f"{a} + {b} = {a + b}")      # Addition
print(f"{a} - {b} = {a - b}")      # Subtraktion  
print(f"{a} * {b} = {a * b}")      # Multiplikation
print(f"{a} / {b} = {a / b}")      # Division
print(f"{a} // {b} = {a // b}")    # Ganzzahl-Division
print(f"{a} % {b} = {a % b}")      # Modulo
print(f"{a} ** {b} = {a ** b}")    # Potenz

# Vergleichsoperatoren
print("\n=== Vergleichsoperatoren ===")
x, y = 10, 20
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} <= {y}: {x <= y}")
print(f"{x} >= {y}: {x >= y}")

# Logische Operatoren
print("\n=== Logische Operatoren ===")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")
print(f"not False: {not False}")

# Zuweisungsoperatoren
print("\n=== Zuweisungsoperatoren ===")
counter = 10
print(f"Start: {counter}")
counter += 5
print(f"Nach += 5: {counter}")
counter -= 3
print(f"Nach -= 3: {counter}")
counter *= 2
print(f"Nach *= 2: {counter}")
counter //= 4
print(f"Nach //= 4: {counter}")
