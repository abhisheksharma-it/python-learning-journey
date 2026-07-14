# STRINGS (Aksharon ki maala - Jaise "Abhishek")

data = "Hello, World!"
name = "Abhishek"

print("----- INDEXING (Position nikalna) -----")
print(f"String: {data}")
print(f"First character (0): {data[0]}")    # H
print(f"Last character (-1): {data[-1]}")   # !

print("\n----- SLICING (Tukda nikalna) -----")
print(f"Full: {data[0:]}")           # Hello, World!
print(f"Sirf Hello: {data[:5]}")     # Hello
print(f"Sirf World: {data[7:12]}")   # World

print("\n----- STRING METHODS (Functions) -----")
text = "  Abhishek Sharma  "
print(f"Original: '{text}'")
print(f"Strip (side ke space hataye): '{text.strip()}'")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}")

print("\n----- ESCAPE SEQUENCES (Special Effects) -----")
print("Hello\nWorld")   # New line (nayi line mein)
print("Hello\tWorld")   # Tab (kuch jagah chhod kar)
print("He said, \"Python is fun!\"")  # Double quote ke andar double quote