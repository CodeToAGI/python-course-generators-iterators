"""
CodeToAGI - Episode 27
Challenge Solution

Topics:

1. Fibonacci Generator
2. Running Minimum Generator
3. itertools.islice
4. Lazy Log Parser
5. Memory Comparison
   """

import itertools
import sys

# ==================================================

# 1. Fibonacci Generator

# ==================================================

def fibonacci():
a, b = 0, 1

```
while True:
    yield a
    a, b = b, a + b
```

print("FIRST 10 FIBONACCI NUMBERS")

fib = fibonacci()

for _ in range(10):
print(next(fib))

# ==================================================

# 2. Running Minimum Generator

# ==================================================

def running_min(iterable):
iterator = iter(iterable)

```
try:
    current_min = next(iterator)
except StopIteration:
    return

yield current_min

for item in iterator:
    current_min = min(current_min, item)
    yield current_min
```

print("\nRUNNING MINIMUM")

numbers = [8, 3, 7, 2, 9, 1]

print(list(running_min(numbers)))

# ==================================================

# 3. First 20 Fibonacci Numbers with islice

# ==================================================

print("\nFIRST 20 FIBONACCI NUMBERS")

first_twenty = list(
itertools.islice(
fibonacci(),
20
)
)

print(first_twenty)

# ==================================================

# 4. Lazy Log Parser

# ==================================================

def error_lines(filename):

```
with open(filename, "r", encoding="utf-8") as f:

    for line in f:

        if "ERROR" in line:
            yield line.strip()
```

print("\nERROR LOG ENTRIES")

try:
for line in error_lines("sample.log"):
print(line)

except FileNotFoundError:
print("sample.log not found")

# ==================================================

# 5. Memory Comparison

# ==================================================

print("\nMEMORY COMPARISON")

fib_generator = fibonacci()

fib_list = list(
itertools.islice(
fibonacci(),
10000
)
)

generator_size = sys.getsizeof(fib_generator)
list_size = sys.getsizeof(fib_list)

print(f"Generator Size : {generator_size:,} bytes")
print(f"List Size      : {list_size:,} bytes")

if generator_size:
ratio = list_size / generator_size

```
print(
    f"List uses approximately "
    f"{ratio:.0f}x more memory"
)
```
