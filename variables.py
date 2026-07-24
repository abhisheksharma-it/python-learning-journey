"""name = "Abhishek"
print(f"My name is {name}")
age = 31 

print (f"My age is {age}")
price = 99.99

print(f"the price is {price}")  #the comment single line comment

#Arithmatic operators 
 
a = 2 
b = 2 
sum = a + b
print(f"the sum of {a} and {b} is {sum}")
print (a - b)
print (a * b)
print (a / b)   
print (a % b)  #modulus operator

#Relational operators

x = 10
y = 20

print(f"Is {x} equal to {y}? {x == y}")
print(f"Is {x} not equal to {y}? {x != y}")
print(f"Is {x} greater than {y}? {x > y}")
print(f"Is {x} less than {y}? {x < y}")
print(f"Is {x} greater than or equal to {y}? {x >= y}")
print(f"Is {x} less than or equal to {y}? {x <= y}")

#Assignment operators

num = 5
print(f"num = {num}")
print(f"num += 3: {num + 3}")
print(f"num -= 2: {num - 2}")  

#Logical operators
a = True
b = False   
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

#Type conversion
num_str = "10"
num_int = int(num_str)
print(f"Converted string '{num_str}' to integer: {num_int}")

#Input from user

input_value = input("Enter a number: ")
print(input_value)
name = input ("Enter Your name: ")

print ("welcome :",name)

#Modules and Packages 



pip install <package_name>  #to install a package  

pip install requests  #to install requests package

pip install numpy  #to install numpy package

pip install pandas  #to install pandas package

pip install matplotlib  #to install matplotlib package

pip install seaborn  #to install seaborn package

pip install scikit-learn  #to install scikit-learn package

pip install tensorflow  #to install tensorflow package

#Escape sequences

print("Hello\nWorld")  #New line
print("Hello\tWorld")  #Tab space 
print("Hello\\World")  #Backslash
print("Hello\'World")  #Single quote    
print("Hello\"World")  #Double quote
print("Hello\rWorld")  #Carriage return
print("Hello\bWorld")  #Backspace
print("Hello\fWorld")  #Form feed
print("Hello\vWorld")  #Vertical tab
print("Hello\0World")  #Null character

#Calculator program with +-*/ 

a  = 1
b = 2

print ("the value of a+b is :",a+b)  #Addition
print ("the value of a-b is :",a-b)  #Subtraction
print ("the value of a*b is :",a*b)  #Multiplication
print ("the value of a/b is :",a/b)  #Division
print ("the value of a%b is :",a%b)  #Modulus

#type conversion
num_str = "10"
num_int = int(num_str)
print(f"Converted string '{num_str}' to integer: {num_int}")


#Strings   STRINGS ARE IMMUTABLE IN PYTHON

name = "Abhishek"
print(f"My name is {name}")

data = "Hello, World!"
print(f"Original string: {data}")     

#Indexing
print(f"First character: {data[0]}")
print(f"Last character: {data[-1]}")   
print(f"Substring (0-4): {data[0:10]}")

#loop through string
for char in data:
    print(char)

    #String slicing
    print(f"Substring (2-7): {data[2:8]}")
    print (f"Substring (start to 5): {data[:6]}")
    print(f"Substring (7 to end): {data[7:]}")


    #String methods
text = "ABHISHEK"
print(f"Original string: {text}") 
print(f"Uppercase: {text.upper()}")  
print(f"Lowercase: {text.lower()}")
print(f"Title Case: {text.title()}") 
print(f"Count of 'o': {text.count('o')}")
print(f"Find 'World': {text.find('World')}")
print(f"Replace 'World' with 'Python': {text.replace('World', 'Python')}")
print(f"Split by comma: {text.split(',')}")
print(f"Strip whitespace: {'   Hello   '.strip()}")
print(f"Is alphanumeric: {text.isalnum()}")
print(f"Is alphabetic: {text.isalpha()}")
print(f"Is digit: {'123'.isdigit()}")
print(f"Is lowercase: {text.islower()}")
print(f"Is uppercase: {text.isupper()}")
print(f"Is space: {'   '.isspace()}")
print(f"Is title case: {'Hello World'.istitle()}")
print(f"Is printable: {text.isprintable()}")
print(f"Is identifier: {'variable_name'.isidentifier()}")
print(f"Is decimal: {'123.45'.isdecimal()}")
print(f"Is numeric: {'123'.isnumeric()}")
print(f"Is casefold: {text.casefold()}")
print(f"Is startswith 'AB': {text.startswith('AB')}")
print(f"Is endswith 'EK': {text.endswith('EK')}")
print(f"Is partition: {text.partition('H')}")
print(f"Is rpartition: {text.rpartition('H')}")
print(f"Is center: {text.center(20, '*')}")
print(f"Is ljust: {text.ljust(20, '-')}")
print(f"Is rjust: {text.rjust(20, '-')}")
print(f"Is zfill: {'42'.zfill(5)}")
print(f"Is count of 'A': {text.count('A')}")
print(f"Is swapcase: {text.swapcase()}")

#conditional statements

#If statement (sirf ek condition check karta hai)

age = 18
if age >= 18:
    print("You are eligible to vote.")

    
    #If-Else statement(do condition check karta hai)

age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


    #If elif-Else statement(multiple condition check karta hai)

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

#match statement
x = 2
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x is something else")

        #loops #for loops

name = "Abhishek"
for c in name: 
 print(c)  #indentation is important in python in for loop)
 
  #range() function 

for x in range(5,99):  #start, stop
 print(x)

for i in range(2, 10, 2):  #start, stop, step
  print(i)
    
    #while loops
i = 0
while i < 5:
    print(i)   #indentation is important in python in while loop if any statement is not indented then it will give an error
    i += 1
print ("Loop finished") #indentation removed from this line so it will print after the loop is finished


#else statement with while loop

i = 0
while i < 5:
    print(i)
    i += 1
else:
 print("Loop finished")

#break and continue statements

#break statement

for dish in range(1, 11): # 1 se 10 tak dishes
     if dish == 5:
        print("Pet bhar gaya! Buffet se bahar aa gaye.")
        break  # Loop yahan poori tarah ruk jayega
    
     print(f"Dish {dish} kha li.")

#continue statement

for dish in range(1, 11): # 1 se 10 tak dishes
 
     if dish == 5:
        print("Eww, Karela! Isko skip karte hain.")
        continue  # Sirf dish 5 skip hogi, loop aage chalta rahega
    
     print(f"Dish {dish} kha li.")

#function 


#function definition
def calculate_sum(a, b): #parameter a and b
 sum = a + b
 print(sum)

calculate_sum(5, 10)  # Function call with arguments 5 and 10

calculate_sum(20, 30)  # Function call with arguments 20 and 30

def greet(name):
    print(f"Hello, {name}!")    
greet("Abhishek")  # Calling the function with the name "Abhishek" 
greet("Alice")  # Calling the function with the name "Alice"
greet("dog")  # Calling the function with the name "Bob"    


#function arguments

#Positional Arguments (Line se aane wale)

from inspect import Arguments


def make_sandwich(item1, item2):
    print(f"I made a sandwich with {item1} and {item2}")

# Sahi order
make_sandwich("Bread", "Cheese") 
# Output: I made a sandwich with Bread and Cheese

# Galat order (Python error nahi dega, par matlab badal jayega)
make_sandwich("Cheese", "Bread") 
# Output: I made a sandwich with Cheese and Bread (Weird!)


#Keyword Arguments (Naam le kar bulana)
# [Kabhi kabhi hum order bhool jate hain. Toh hum Python ko direct naam bata kar value de sakte hain. Agar aap naam bata doge, toh order matter nahi karega.]


def make_sandwich(item1, item2):
    print(f"I made a sandwich with {item1} and {item2}")

# Order change kar diya, par naam de diya toh Python samajh jayega
make_sandwich(item2="Cheese", item1="Bread") 
# Output: I made a sandwich with Bread and Cheese


#Default Arguments (Pehle se set kiye hue)

# Yahan 'sugar' ki default value 2 set kar di hai
def make_tea(type_of_tea, sugar=2):
    print(f"Here is your {type_of_tea} with {sugar} spoons of sugar.")

# Sirf chai ka type bataya, sugar nahi batayi (Default use hoga)
make_tea("Masala Chai") 
# Output: Here is your Masala Chai with 2 spoons of sugar.

# Dono bataye (Aapki di hui value use hogi)
make_tea("Green Tea", sugar=0) 
# Output: Here is your Green Tea with 0 spoons of sugar.

#Positional: Order se dena padta hai.

#Keyword: Naam likh kar dena padta hai (Order aage-peeche kar sakte ho).


#Default: Agar kuch na do, toh khud se assume kar leta hai.


#list in python

my_list = [1, 2, 3, 4, 5 , 6 ,2] #unordered collection of items, ordered, changeable, allows duplicate members
print(my_list)

#list indexing
print(my_list[0])  #first item
print(my_list[1])  #second item
print(my_list[2])  #third item 

#list slicing
print(my_list[0:3])  #first three items
print(my_list[3:])  #items from index 3 to end
print(my_list[:3])  #items from start to index 3

#list methods
my_list.append(7)  #add item to end of list
print(my_list)

my_list.insert(0, 0)  #add item at index 0
print(my_list)

my_list.remove(2)  #remove first occurrence of item

#tuple in python

my_tuple = (1, 2, 3,)  #ordered, changeable, allows duplicate members
print(my_tuple) 
a, b, c = my_tuple  #unpacking
print(a, b, c)

#tuple indexing
print(my_tuple[0])  #first item
print(my_tuple[1])  #second item    
print(my_tuple[2])  #third item 


#tuple slicing
print(my_tuple[0:3])  #first three items
print(my_tuple[3:])  #items from index 3 to end
print(my_tuple[:3])  #items from start to index 3   

#tuple methods
my_tuple.append(7)  #add item to end of list
print(my_tuple) 

#recursive function

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)    
print(factorial(5))  #factorial of 5 is 120 

#recursive function with base case

a = 1
b = 2
def fibonacci(n):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

#dictionary in python
a = 1
b = 2
c = 3
d = 4
my_dict = {a: b, c: d}  #unordered collection of key-value pairs, ordered, changeable, allows duplicate keys
print(my_dict)

#dictionary indexing

print(my_dict[a])  #first item
print(my_dict[c])  #third item  


#dictionary methods
my_dict.update({a: b})  #add item to end of list
print(my_dict)

my_dict.pop(c)  #remove first occurrence of item
print(my_dict)

my_dict.popitem()  #remove first key-value pair
print(my_dict)

my_dict.clear()  #remove all key-value pairs
print(my_dict)

#set in python

set1 = {1, 2, 3, 4, 5, 6, 2}  #unordered collection of unique items, ordered, changeable, allows duplicate members
print(set1)

#exception handling

#try: Isme wo code likho jisme error aane ka dar ho.

#except: Agar error aa jaye, toh kya karna hai, wo yahan likho.


fruits = ["Apple", "Mango"]

try:
    # Yahan galti hogi kyunki list mein 5th number par kuch nahi hai
    print(fruits[5]) 
    
except:
    # Program crash hone ke bajaye shanti se ye print kar dega
    print("Bhai, list mein itne item nahi hain!")

#finally: Isme wo code likho jisme error aane ka dar ho.


fruits = ["Apple", "Mango"]

try:
    # Yahan galti hogi kyunki list mein 5th number par kuch nahi hai
    print(fruits[5])

    print("Bhai, list mein itne item nahi hain!")
    
except:
    # Program crash hone ke bajaye shanti se ye print kar dega
    print("Bhai, list mein itne item nahi hain!")
    
finally:
    # Isme wo code likho jisme error aane ka dar ho.
    print("Bhai, list mein itne item nahi hain!")

    #custom error
try:
    # Yahan galti hogi kyunki list mein 5th number par kuch nahi hai
    print(fruits[5])
except IndexError:
    # Program crash hone ke bajaye shanti se ye print kar dega
    print("Bhai, list mein itne item nahi hain!")
else:
    # Isme wo code likho jisme error aane ka dar ho.
    print("Bhai, list mein itne item nahi hain!")   """

#virtual environment : Apne Python projects ke liye alag-alag 'kamaray' (isolated boxes) banana.

#pip install virtualenv
#virtualenv venv
#venv\Scripts\activate

#os module : Apne Python code se computer (Operating System) ke files aur folders ko control karna.
import os
print(os.getcwd())  #current working directory

#file input/output in python




