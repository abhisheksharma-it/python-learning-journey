class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Zero se divide nahi kar sakte!"
        return a / b


# --- Main Program ---
calc = Calculator()  # Object banaya

num1 = float(input("Pehla number: "))
op = input("Sign (+, -, *, /): ")
num2 = float(input("Doosra number: "))

if op == '+':
    print("Result:", calc.add(num1, num2))
elif op == '-':
    print("Result:", calc.subtract(num1, num2))
elif op == '*':
    print("Result:", calc.multiply(num1, num2))
elif op == '/':
    print("Result:", calc.divide(num1, num2))
else:
    print("Galat sign daala hai!")
