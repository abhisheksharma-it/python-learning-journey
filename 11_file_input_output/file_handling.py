# Topic 11: File Input & Output in Python

# 1. File me data write karna ('w' mode)
with open("sample.txt", "w") as file:
    file.write("Hello! Welcome to Python Learning Journey.\n")
    file.write("This file is created using Python File Handling.\n")

print("File successfully created and written.")

# 2. Existing file me new line add karna ('a' append mode)
with open("sample.txt", "a") as file:
    file.write("Appending a new line at the end of the file.\n")

# 3. File ka content read karna ('r' read mode)
with open("sample.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)
