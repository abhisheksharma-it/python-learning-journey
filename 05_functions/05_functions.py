# FUNCTIONS (Code ka dabba - Baar baar use karo)

# 1. SIMPLE FUNCTION
print("----- SIMPLE FUNCTION -----")
def greet(name):
    print(f"Namaste, {name}!")

greet("Abhishek")
greet("Priya")

# 2. FUNCTION WITH RETURN (Jo result wapas de)
print("\n----- FUNCTION WITH RETURN -----")
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# 3. DEFAULT ARGUMENTS (Agar value na do toh default)
print("\n----- DEFAULT ARGUMENTS -----")
def make_chai(type="Masala", sugar=2):
    print(f"{type} chai with {sugar} spoons of sugar.")

make_chai()                # Default wali
make_chai("Green", 0)      # Custom wali

# 4. RECURSION (Khud ko call karna - Jaise Factorial)
print("\n----- RECURSION (Factorial) -----")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")  # 5*4*3*2*1 = 120