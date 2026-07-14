# Variables and Data Types

name = "Abhishek"  # String (Text)
age = 31           # Integer (Number)
price = 99.99      # Float (Number)
is_student = True  # Boolean (Sahi/Galat)

print(f"My name is {name}")
print(f"My age is {age}")
print(f"The price is {price}")
print(f"Is student: {is_student}")

# Type Conversion  (Ek type se doosra type mein badalna)

num_str = "10"            
num_int = int(num_str)    
print(f"Converted string to integer: {num_int}")

# User Input (User se baat karna)
user_name = input("Enter your name: ")
print(f"Welcome: {user_name}")

# 4. Dynamic Type Checking
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of price: {type(price)}")