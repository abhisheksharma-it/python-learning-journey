# ==========================================================
# 1. CLASS & OBJECT 
# ==========================================================

class Student:
    def __init__(self, name, roll_no):
        self.name = name          # Attribute
        self.roll_no = roll_no    # Attribute

    def display(self):            # Method
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}")

# Object Creation:
student1 = Student("Rahul Sharma", 101)  # Real Instance (Object)
student1.display()


# ==========================================================
# 2. ENCAPSULATION (Data Hiding & Protection)
# ==========================================================
# Variables ko private ('__') karke direct access se bachana.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # Private attribute

    # Getter (Salary dekhne ke liye)
    def get_salary(self):
        return self.__salary

    # Setter (Salary safe tareeqe se update karne ke liye)
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print(f"Updated Salary: ₹{self.__salary}")
        else:
            print("Invalid salary amount!")


# ==========================================================
# 3. INHERITANCE (Code Reusability)
# ==========================================================
# Parent class ki properties ko Child class me reuse karna.

class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal): # Dog class, Animal ko inherit kar rahi hai
    def bark(self):
        print("Dog barks: Woof Woof!")


# ==========================================================
# 4. POLYMORPHISM (Same Function, Different Behavior)
# ==========================================================
# Same method name, par har class me apna alag kaam.

class Cat(Animal):
    # Parent class ke 'eat' method ko override kar rahe hain
    def eat(self):
        print("Cat drinks milk.")


# ==========================================================
# 5. ABSTRACTION (Hiding Background Logic)
# ==========================================================
# Sirf essential features dikhana, implementation detail chhupana.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Implementation child class karegi

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with Key!")


# ==========================================================
# DRIVER CODE (Testing All Concepts)
# ==========================================================
if __name__ == "__main__":
    print("\n--- 1. Class & Object ---")
    s2 = Student("Ankit Verma", 102)
    s2.display()

    print("\n--- 2. Encapsulation ---")
    emp = Employee("Priya", 50000)
    print("Current Salary:", emp.get_salary())
    emp.set_salary(55000)

    print("\n--- 3. Inheritance ---")
    d = Dog()
    d.eat()   # Parent ka method
    d.bark()  # Apna method

    print("\n--- 4. Polymorphism ---")
    c = Cat()
    c.eat()   # Same method name 'eat', par behavior Cat wala

    print("\n--- 5. Abstraction ---")
    my_car = Car()
    my_car.start_engine()
