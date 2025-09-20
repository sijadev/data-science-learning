# 5.2 Scope and Namespaces - Code Examples

# ========================================
# Global vs. Local Variables
# ========================================
print("=" * 50)
print("GLOBAL VS. LOCAL VARIABLES")
print("=" * 50)

# Global variable
global_var = "I am global"

def show_variables():
    # Local variable
    local_var = "I am local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

show_variables()
print(f"Outside function - Global: {global_var}")

# Try to access local variable
try:
    print(f"Outside function - Local: {local_var}")
except NameError as e:
    print(f"Error: {e}")

# ========================================
# Variable Shadowing
# ========================================
print("\n" + "=" * 50)
print("VARIABLE SHADOWING")
print("=" * 50)

name = "Global Alice"

def shadow_example():
    name = "Local Alice"  # Shadows global variable
    print(f"In function: {name}")

print(f"Before function: {name}")
shadow_example()
print(f"After function: {name}")  # Global unchanged

# ========================================
# LEGB Rule
# ========================================
print("\n" + "=" * 50)
print("LEGB RULE (Local, Enclosing, Global, Built-in)")
print("=" * 50)

# Built-in: len, print, etc.
x = "Global x"

def outer():
    x = "Enclosing x"

    def inner():
        x = "Local x"
        print(f"1. Local: {x}")

        # Access enclosing scope
        def deep_inner():
            print(f"2. Enclosing: {x}")  # Finds enclosing x

        deep_inner()

    inner()
    print(f"3. In outer: {x}")

outer()
print(f"4. Global: {x}")

# Built-in example
def show_builtin():
    # len is built-in function
    print(f"Built-in len([1,2,3]): {len([1, 2, 3])}")

show_builtin()

# ========================================
# global Keyword
# ========================================
print("\n" + "=" * 50)
print("GLOBAL KEYWORD")
print("=" * 50)

counter = 0  # Global variable

def increment_counter():
    global counter  # Access global variable
    counter += 1
    print(f"Counter in function: {counter}")

print(f"Counter before functions: {counter}")
increment_counter()
increment_counter()
print(f"Counter after functions: {counter}")

# Without global - would cause error
def wrong_increment():
    try:
        counter += 1  # UnboundLocalError!
    except UnboundLocalError as e:
        print(f"Error without global: {e}")

wrong_increment()

# ========================================
# nonlocal Keyword
# ========================================
print("\n" + "=" * 50)
print("NONLOCAL KEYWORD")
print("=" * 50)

def create_counter():
    count = 0

    def increment():
        nonlocal count  # Access enclosing variable
        count += 1
        return count

    def get_count():
        return count

    def reset():
        nonlocal count
        count = 0

    return increment, get_count, reset

# Create counter
inc, get, reset = create_counter()

print(f"Initial: {get()}")
print(f"After increment: {inc()}")
print(f"After increment: {inc()}")
print(f"After increment: {inc()}")
print(f"Current value: {get()}")
reset()
print(f"After reset: {get()}")

# ========================================
# Namespace Examples
# ========================================
print("\n" + "=" * 50)
print("NAMESPACE EXAMPLES")
print("=" * 50)

# globals() and locals()
global_test = "Global value"

def namespace_demo():
    local_test = "Local value"

    print("Global namespaces (excerpt):")
    global_ns = globals()
    for key in ['global_test', '__name__', 'namespace_demo']:
        if key in global_ns:
            print(f"  {key}: {global_ns[key]}")

    print("\nLocal namespaces:")
    local_ns = locals()
    for key, value in local_ns.items():
        print(f"  {key}: {value}")

namespace_demo()

# ========================================
# Closures
# ========================================
print("\n" + "=" * 50)
print("CLOSURES")
print("=" * 50)

def create_multiplier(factor):
    """Creates a function that multiplies by factor."""
    def multiplier(number):
        return number * factor  # factor from enclosing scope
    return multiplier

# Create different multipliers
double = create_multiplier(2)
triple = create_multiplier(3)
quad = create_multiplier(4)

number = 5
print(f"double({number}) = {double(number)}")
print(f"triple({number}) = {triple(number)}")
print(f"quad({number}) = {quad(number)}")

# Closure with mutable state
def create_accumulator(start=0):
    total = start

    def add(value):
        nonlocal total
        total += value
        return total

    def get_total():
        return total

    def reset():
        nonlocal total
        total = start

    return add, get_total, reset

acc_add, acc_get, acc_reset = create_accumulator(10)

print(f"\nAccumulator start: {acc_get()}")
print(f"After add(5): {acc_add(5)}")
print(f"After add(3): {acc_add(3)}")
print(f"After add(2): {acc_add(2)}")
acc_reset()
print(f"After reset: {acc_get()}")

# ========================================
# Decorators (Simple Example)
# ========================================
print("\n" + "=" * 50)
print("DECORATORS (SIMPLE EXAMPLE)")
print("=" * 50)

def simple_decorator(func):
    """A simple decorator."""
    def wrapper():
        print("Before the function")
        result = func()
        print("After the function")
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("Hello from the decorated function!")
    return "Done"

result = say_hello()
print(f"Return value: {result}")

# Manual decorator (equivalent to @)
def say_goodbye():
    print("Goodbye!")
    return "Bye"

decorated_goodbye = simple_decorator(say_goodbye)
print("\nManually decorated:")
decorated_goodbye()

# ========================================
# Module-Level Variables
# ========================================
print("\n" + "=" * 50)
print("MODULE-LEVEL VARIABLES")
print("=" * 50)

# These variables are at module level
MODULE_NAME = "Scope and Namespaces Example"
VERSION = "1.0"

def get_module_info():
    """Shows module information."""
    print(f"Module: {MODULE_NAME}")
    print(f"Version: {VERSION}")
    print(f"__name__: {__name__}")

get_module_info()

# ========================================
# Practical Applications
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL APPLICATIONS")
print("=" * 50)

# Configuration pattern
APP_CONFIG = {
    "debug": True,
    "database_url": "sqlite:///app.db",
    "secret_key": "secret123"
}

def get_config(key):
    """Safe access to configuration."""
    return APP_CONFIG.get(key, "Not found")

def update_config(key, value):
    """Updates configuration."""
    global APP_CONFIG
    APP_CONFIG[key] = value

print(f"Debug mode: {get_config('debug')}")
update_config('debug', False)
print(f"Debug mode after update: {get_config('debug')}")

# Factory pattern with closures
def create_validator(min_length=1, max_length=100):
    """Creates a string validator."""
    def validate(text):
        if not isinstance(text, str):
            return False, "Must be a string"
        if len(text) < min_length:
            return False, f"Too short (min: {min_length})"
        if len(text) > max_length:
            return False, f"Too long (max: {max_length})"
        return True, "Valid"
    return validate

# Different validators
username_validator = create_validator(3, 20)
password_validator = create_validator(8, 50)

test_strings = ["ab", "alice", "very_long_username_that_is_too_long", "password123"]

print("\nUsername validation:")
for s in test_strings:
    valid, message = username_validator(s)
    print(f"  '{s}': {valid} - {message}")

# ========================================
# Debugging Scopes
# ========================================
print("\n" + "=" * 50)
print("DEBUGGING SCOPES")
print("=" * 50)

def debug_scope():
    """Helper function for debugging scopes."""
    local_var = "Local"

    def show_vars():
        nested_var = "Nested"
        print("=== Scope Debug ===")
        print(f"Built-ins available: {len(dir(__builtins__))}")
        print(f"Global variables: {len(globals())}")
        print(f"Local variables: {list(locals().keys())}")

        # Check specific variables
        for var_name in ['local_var', 'nested_var', 'global_var']:
            try:
                value = locals().get(var_name) or globals().get(var_name)
                if value:
                    print(f"  {var_name}: {value}")
            except:
                print(f"  {var_name}: Not found")

    show_vars()

debug_scope()

# ========================================
# Best Practices
# ========================================
print("\n" + "=" * 50)
print("BEST PRACTICES")
print("=" * 50)

# 1. Minimize global variables
class AppState:
    """Better than global variables."""
    def __init__(self):
        self.user_count = 0
        self.is_running = True

    def increment_users(self):
        self.user_count += 1

app_state = AppState()

# 2. Use closures for private data
def create_secure_counter():
    """Counter with private data."""
    _count = 0  # "Private" through naming convention

    def increment():
        nonlocal _count
        _count += 1
        return _count

    def get_count():
        return _count

    # _count is not directly accessible from outside
    return increment, get_count

secure_inc, secure_get = create_secure_counter()
print(f"Secure counter: {secure_inc()}, {secure_inc()}, {secure_get()}")

# 3. Explicit parameters instead of global access
def calculate_tax(amount, tax_rate=0.19):
    """Better than using global TAX_RATE."""
    return amount * tax_rate

print(f"Tax for 100€: {calculate_tax(100):.2f}€")

print("\nScope and namespace examples completed!")