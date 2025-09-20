# 🔀 Conditional Statements

## if Statement

The if statement allows code to be executed only under certain conditions.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## if-elif-else Chain

For multiple conditions we use elif (else if):

```python
if grade >= 90:
    rating = "Excellent"
elif grade >= 80:
    rating = "Very good"
elif grade >= 70:
    rating = "Good"
else:
    rating = "Needs improvement"
```

## Comparison Operators

- `==` Equal
- `!=` Not equal
- `<` Less than
- `>` Greater than
- `<=` Less than or equal
- `>=` Greater than or equal

## Logical Operators

- `and` And operation
- `or` Or operation
- `not` Negation

## Ternary Operator

Short syntax for simple if-else statements:

```python
status = "active" if age >= 18 else "inactive"
```