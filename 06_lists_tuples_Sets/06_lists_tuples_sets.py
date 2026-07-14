# LISTS (Mutable - Badal sakte hain)
print("----- LISTS (Badal sakte hain) -----")
fruits = ["Apple", "Banana", "Mango"]
print(f"Original: {fruits}")

fruits.append("Orange")       # End mein jodna
print(f"After Append: {fruits}")

fruits.insert(1, "Kiwi")      # Beech mein ghusedna
print(f"After Insert: {fruits}")

fruits.remove("Banana")       # Hatao
print(f"After Remove: {fruits}")

# TUPLES (Immutable - Badal nahi sakte)
print("\n----- TUPLES (Badal nahi sakte) -----")
colors = ("Red", "Green", "Blue")
print(f"Tuple: {colors}")
print(f"First Color: {colors[0]}")

# SETS (Unique values - Sirf ek baar aata hai)
print("\n----- SETS (Duplicate nahi) -----")
numbers = {1, 2, 3, 4, 5, 5, 5}  # 5 sirf ek baar aayega
print(f"Set: {numbers}")

numbers.add(6)
print(f"After Add: {numbers}")