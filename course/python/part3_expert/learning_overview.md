# Part 3: Python Experte - Learning Overview

## Modul 11: Concurrent Programming

### 11.1 Threading
```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import queue

# Basic Thread
def worker(name, seconds):
    print(f"Worker {name} starting")
    time.sleep(seconds)
    print(f"Worker {name} done")

thread1 = threading.Thread(target=worker, args=("A", 2))
thread2 = threading.Thread(target=worker, args=("B", 1))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

# Thread Pool
def process_item(item):
    return item ** 2

with ThreadPoolExecutor(max_workers=4) as executor:
    items = range(10)
    results = list(executor.map(process_item, items))

# Thread Synchronization
lock = threading.Lock()
shared_counter = 0

def increment_counter():
    global shared_counter
    with lock:
        temp = shared_counter
        time.sleep(0.001)
        shared_counter = temp + 1

# Producer-Consumer Pattern
q = queue.Queue()

def producer():
    for i in range(5):
        q.put(f"item_{i}")
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")
        q.task_done()
```

### 11.2 Multiprocessing
```python
import multiprocessing
from multiprocessing import Pool, Process, Queue, Manager
import os

# Basic Process
def process_function(name):
    print(f"Process {name}, PID: {os.getpid()}")

if __name__ == "__main__":
    processes = []
    for i in range(4):
        p = Process(target=process_function, args=(f"P{i}",))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # Process Pool
    def compute_square(n):
        return n * n

    with Pool(processes=4) as pool:
        numbers = range(10)
        results = pool.map(compute_square, numbers)

    # Shared Memory
    manager = Manager()
    shared_list = manager.list()
    shared_dict = manager.dict()

    def worker_shared(shared_list, shared_dict, key, value):
        shared_list.append(value)
        shared_dict[key] = value

    # Inter-Process Communication
    def sender(conn):
        conn.send(['data', 42, None])
        conn.close()

    def receiver(conn):
        data = conn.recv()
        print(f"Received: {data}")
        conn.close()

    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))
```

### 11.3 Async Programming
```python
import asyncio
import aiohttp
import aiofiles

# Basic Async Function
async def hello_async():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Multiple Coroutines
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'http://api.example.com/data1',
        'http://api.example.com/data2',
        'http://api.example.com/data3'
    ]

    # Concurrent execution
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)

    # Sequential execution
    for url in urls:
        result = await fetch_data(url)

# Async File I/O
async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as file:
        contents = await file.read()
        return contents

# Async Context Manager
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(0.5)

# Event Loop
async def periodic_task():
    while True:
        print("Running periodic task")
        await asyncio.sleep(5)

# Run async code
asyncio.run(main())
```

## Modul 12: Data Science Stack

### 12.1 NumPy
```python
import numpy as np

# Array Creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 4))
arr4 = np.arange(0, 10, 2)
arr5 = np.linspace(0, 1, 5)
arr6 = np.random.randn(3, 3)

# Array Operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise operations
c = a + b
d = a * b
e = a ** 2

# Matrix operations
f = a.dot(b)  # or a @ b
g = a.T  # Transpose

# Broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_scaled = arr * 2
arr_added = arr + np.array([10, 20, 30])

# Indexing and Slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
element = arr[1, 2]  # 6
row = arr[1, :]  # [4, 5, 6]
column = arr[:, 1]  # [2, 5, 8]
subset = arr[:2, 1:]  # [[2, 3], [5, 6]]

# Boolean Indexing
mask = arr > 5
filtered = arr[mask]

# Statistical Operations
mean = arr.mean()
std = arr.std()
min_val = arr.min()
max_val = arr.max()
sum_val = arr.sum(axis=0)  # Sum along columns

# Linear Algebra
matrix = np.array([[1, 2], [3, 4]])
det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
```

### 12.2 Pandas
```python
import pandas as pd

# DataFrame Creation
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chicago']
})

# Reading Data
df_csv = pd.read_csv('data.csv')
df_excel = pd.read_excel('data.xlsx')
df_json = pd.read_json('data.json')

# Data Exploration
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes

# Selection and Filtering
column = df['Name']
multiple_columns = df[['Name', 'Age']]
row_by_index = df.iloc[0]
row_by_label = df.loc[0]
filtered = df[df['Age'] > 25]

# Data Manipulation
df['NewColumn'] = df['Age'] * 2
df.drop('NewColumn', axis=1, inplace=True)
df.rename(columns={'Name': 'FullName'}, inplace=True)
df.sort_values('Age', ascending=False)

# GroupBy Operations
grouped = df.groupby('City')
aggregated = grouped.agg({
    'Age': ['mean', 'max'],
    'Name': 'count'
})

# Merge and Join
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})

merged = pd.merge(df1, df2, on='key', how='inner')
outer_merged = pd.merge(df1, df2, on='key', how='outer')

# Time Series
dates = pd.date_range('2024-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(100), index=dates)
monthly = ts.resample('M').mean()

# Missing Data
df.fillna(0)
df.dropna()
df.interpolate()
```

### 12.3 Matplotlib & Seaborn
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib Basics
fig, ax = plt.subplots(figsize=(10, 6))

# Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, label='sin(x)')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Sine Wave')
ax.legend()
ax.grid(True)

# Multiple Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, np.sin(x))
axes[0, 1].scatter(x[:20], y[:20])
axes[1, 0].bar(['A', 'B', 'C'], [1, 2, 3])
axes[1, 1].hist(np.random.randn(1000), bins=30)

# Seaborn Statistical Plots
tips = sns.load_dataset('tips')

# Distribution Plots
sns.histplot(data=tips, x='total_bill', kde=True)
sns.boxplot(data=tips, x='day', y='total_bill')
sns.violinplot(data=tips, x='day', y='total_bill')

# Relationship Plots
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
sns.regplot(data=tips, x='total_bill', y='tip')

# Categorical Plots
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
sns.countplot(data=tips, x='day')

# Heatmap
correlation = tips.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')

# Pair Plot
sns.pairplot(tips, hue='time')

plt.show()
```

## Modul 13: Machine Learning

### 13.1 Scikit-learn Grundlagen
```python
from sklearn import datasets, model_selection, preprocessing
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.pipeline import Pipeline

# Load Data
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train-Test Split
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Preprocessing
scaler = preprocessing.StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Classification
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Cross-Validation
scores = model_selection.cross_val_score(clf, X, y, cv=5)

# Hyperparameter Tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search = model_selection.GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy'
)
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

# Pipeline
pipeline = Pipeline([
    ('scaler', preprocessing.StandardScaler()),
    ('classifier', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)

# Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)
```

### 13.2 Deep Learning mit PyTorch
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Define Neural Network
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

# Prepare Data
X_tensor = torch.FloatTensor(X_train)
y_tensor = torch.LongTensor(y_train)
dataset = TensorDataset(X_tensor, y_tensor)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Initialize Model
model = NeuralNetwork(input_size=4, hidden_size=64, output_size=3)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training Loop
epochs = 100
for epoch in range(epochs):
    for batch_X, batch_y in dataloader:
        # Forward pass
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Evaluation
model.eval()
with torch.no_grad():
    X_test_tensor = torch.FloatTensor(X_test)
    predictions = model(X_test_tensor)
    _, predicted = torch.max(predictions, 1)
    accuracy = (predicted.numpy() == y_test).mean()
```

## Modul 14: Web Development

### 14.1 Flask Framework
```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

# Forms
class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Routes
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/api/users', methods=['GET', 'POST'])
def api_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([u.to_dict() for u in users])

    elif request.method == 'POST':
        data = request.json
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### 14.2 Django Framework
```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .forms import ArticleForm

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 10

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),
]

# serializers.py (Django REST Framework)
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_at']
```

## Modul 15: Advanced Topics

### 15.1 Metaprogramming
```python
# Metaclasses
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

# Descriptors
class ValidatedAttribute:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        setattr(obj, self.name, value)

class Person:
    age = ValidatedAttribute(min_value=0, max_value=150)

    def __init__(self, age):
        self.age = age

# Dynamic Class Creation
def create_class(name, attrs):
    return type(name, (object,), attrs)

DynamicClass = create_class('DynamicClass', {
    'attribute': 42,
    'method': lambda self: "Dynamic method"
})
```

### 15.2 Performance Optimization
```python
# Profiling
import cProfile
import pstats
from line_profiler import LineProfiler

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# cProfile
profiler = cProfile.Profile()
profiler.enable()
result = slow_function()
profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats()

# Memory Profiling
from memory_profiler import profile

@profile
def memory_intensive():
    large_list = [i for i in range(1000000)]
    return sum(large_list)

# Cython Example (in .pyx file)
"""
def fibonacci_cython(int n):
    cdef int a = 0, b = 1, temp
    cdef int i
    cdef list result = []

    for i in range(n):
        result.append(a)
        temp = a + b
        a = b
        b = temp

    return result
"""

# NumPy Optimization
import numpy as np

# Slow: Python loops
def slow_computation(arr):
    result = []
    for item in arr:
        result.append(item ** 2)
    return result

# Fast: Vectorized
def fast_computation(arr):
    return arr ** 2

# Using numba for JIT compilation
from numba import jit

@jit(nopython=True)
def fast_loop(arr):
    result = np.empty_like(arr)
    for i in range(arr.shape[0]):
        result[i] = arr[i] ** 2
    return result
```

### 15.3 Design Patterns
```python
# Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory Pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    def update(self, state):
        pass

# Strategy Pattern
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with credit card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        return self.payment_strategy.pay(amount)

# Decorator Pattern
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1
```

## Best Practices für Part 3

1. **Concurrency**: Wähle das richtige Tool (Threading für I/O, Multiprocessing für CPU, Async für viele I/O)
2. **NumPy/Pandas**: Nutze Vektorisierung statt Schleifen
3. **Machine Learning**: Immer Daten normalisieren und Cross-Validation nutzen
4. **Web Development**: Befolge REST-Prinzipien und nutze ORM
5. **Performance**: Erst messen (profilen), dann optimieren
6. **Design Patterns**: Nutze sie wenn sie passen, nicht erzwingen
7. **Testing**: Schreibe Tests für kritische und komplexe Funktionen

## Weiterführende Ressourcen
- [Python Concurrency](https://realpython.com/python-concurrency/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Design Patterns](https://python-patterns.guide/)