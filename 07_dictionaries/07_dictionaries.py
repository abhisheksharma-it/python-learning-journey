# DICTIONARIES (Key-Value pairs - Jaise real-life dictionary)
print("----- DICTIONARIES (Key-Value) -----")

student = {
    "name": "Abhishek",
    "age": 31,
    "city": "Kangra"
}
print(f"Original: {student}")

# Access karna
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Add karna
student["email"] = "abhi@email.com"
print(f"After Add: {student}")

# Update karna
student["age"] = 32
print(f"After Update: {student}")

# Delete karna
student.pop("city")
print(f"After Delete: {student}")

# Loop through dictionary
print("\n----- LOOP THROUGH DICTIONARY -----")
for key, value in student.items():
    print(f"{key}: {value}")