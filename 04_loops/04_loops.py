# LOOPS (Kaam ko baar-baar karna)   #indentation is important in python in for loop)

print("----- FOR LOOP (List ke items ke liye) -----")
fruits = ["Apple", "Mango", "Banana"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n----- RANGE (Number ka sequence) -----")
for i in range(1, 6):  # 1 se 5 tak
    print(f"Number: {i}")

print("\n----- WHILE LOOP (Jab tak condition true hai) -----")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # count = count + 1

print("\n----- BREAK (Loop todna) -----")
for dish in range(1, 11):
    if dish == 5:
        print("Pet bhar gaya! Break!")
        break
    print(f"Dish {dish} kha li.")

print("\n----- CONTINUE (Ek baar skip karna) -----")
for dish in range(1, 11):
    if dish == 5:
        print("Karela! Skip karte hain.")
        continue
    print(f"Dish {dish} kha li.")