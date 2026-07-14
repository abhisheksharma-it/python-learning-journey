# CONDITIONAL STATEMENTS (if, elif, else, match-case)
# Decision lene ke liye (Jaise - "Agar barish hui toh chata le lo")

print("----- 1. SIMPLE IF (Sirf ek condition) -----")
age = 18
if age >= 18:
    print("Tum vote kar sakte ho!")

print("\n----- 2. IF-ELSE (Do options) -----")
age = 16
if age >= 18:
    print("Tum vote kar sakte ho!")
else:
    print("Tum chhote ho, vote mat karo!")

print("\n----- 3. IF-ELIF-ELSE (Multiple options) -----")
marks = 85
if marks >= 90:
    print("Grade: A (Shaandar!)")
elif marks >= 80:
    print("Grade: B (Bahut accha!)")
elif marks >= 70:
    print("Grade: C (Theek hai)")
else:
    print("Grade: D (Mehnat karo!)")

print("\n----- 4. NESTED IF (Andar wali condition) -----")
is_student = True
is_holiday = False

if is_student:
    if is_holiday:
        print("Chhutti hai! Sone jao.")
    else:
        print("School jao! Padhai karo.")

print("\n----- 5. MATCH-CASE (Switch statement - Python 3.10+) -----")
day = 3
match day:
    case 1:
        print("Monday - Chai aur Coding")
    case 2:
        print("Tuesday - Gym")
    case 3:
        print("Wednesday - Friends ke saath")
    case 4:
        print("Thursday - Office")
    case 5:
        print("Friday - Party")
    case _:  # Else ki tarah
        print("Weekend - Chill kar!")

print("\n----- 6. SHORTHAND IF (Ek line mein) -----")
num = 5
result = "Even" if num % 2 == 0 else "Odd"
print(f"Number {num} is: {result}")