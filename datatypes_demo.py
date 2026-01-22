# datatypes_demo.py
# Task 2: Variables, Data Types & Type Conversion

# 1. Declaring variables of different data types
age = 21                  # int
height = 5.8              # float
name = "Ashok"            # string
is_student = True         # boolean

# 2. Printing values and their types
print("age:", age, "| type:", type(age))
print("height:", height, "| type:", type(height))
print("name:", name, "| type:", type(name))
print("is_student:", is_student, "| type:", type(is_student))

print("-" * 40)

# 3. Arithmetic operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("-" * 40)

# 4. Type conversion from string to int and float
num_str = "25"
decimal_str = "12.5"

num_int = int(num_str)          # string → int
num_float = float(decimal_str)  # string → float

print("Converted int:", num_int, "| type:", type(num_int))
print("Converted float:", num_float, "| type:", type(num_float))

print("-" * 40)

# 5. Handling invalid input using try-except
invalid_input = "abc"

try:
    result = int(invalid_input)
except ValueError:
    print("Error: Cannot convert 'abc' to integer")

print("-" * 40)

# 6. Concatenating strings and numbers properly
marks = 85
print("Marks:", str(marks))   # int → string for concatenation

print("-" * 40)

# 7. Demonstrating dynamic typing
value = 100
print("value:", value, "| type:", type(value))

value = "Now I am a string"
print("value:", value, "| type:", type(value))
