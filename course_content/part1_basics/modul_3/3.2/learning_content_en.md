# 🔄 Loops

## for Loop

The for loop is used to iterate over sequences.

### With range()

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### With Lists

```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
```

### With enumerate()

To get both index and value:

```python
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## while Loop

The while loop runs as long as a condition is true:

```python
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
```

## Loop Control

- `break` - Exits the loop immediately
- `continue` - Skips to the next iteration

## List Comprehensions

Elegant method for creating lists:

```python
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
```