# ⚙️ Defining and Calling Functions

## What are Functions?

Functions are reusable code blocks that perform a specific task.

```python
def greeting():
    print("Hello World!")

greeting()  # Function call
```

## Parameters and Arguments

### Simple Parameters

```python
def greet_person(name):
    print(f"Hello {name}!")

greet_person("Alice")
```

### Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(5, 3)  # 8
```

### Default Values

```python
def greeting(name, time_of_day="day"):
    print(f"Good {time_of_day}, {name}!")

greeting("Alice")           # Good day, Alice!
greeting("Bob", "morning")  # Good morning, Bob!
```

## Return Values

```python
def square(x):
    return x ** 2

result = square(5)  # 25
```

## Variable Arguments

### *args - Variable Number of Arguments

```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

### **kwargs - Variable Keyword Arguments

```python
def person_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person_info(name="Alice", age=30, profession="Developer")
```

## Local vs. Global Variables

```python
global_variable = "I am global"

def test_function():
    local_variable = "I am local"
    print(global_variable)  # Access to global variable
    print(local_variable)   # Access to local variable

test_function()
# print(local_variable)  # Error! Not available outside
```

## Lambda Functions

Short, anonymous functions for simple operations:

```python
square = lambda x: x ** 2
print(square(5))  # 25

# With lists
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

## Best Practices

- Use meaningful function names
- A function should only do one thing
- Use docstrings for documentation
- Avoid too many parameters
- Use Type Hints (modern Python practice)