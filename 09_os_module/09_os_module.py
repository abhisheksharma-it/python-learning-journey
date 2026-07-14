# OS MODULE (Computer ke files/folders ke saath khelna)
import os

print("----- OS MODULE -----")

# Current working directory (Abhi kaunsi folder mein ho)
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# List all files/folders
print("\n----- FILES IN CURRENT DIRECTORY -----")
for item in os.listdir():
    print(f"- {item}")

# New folder banana
try:
    os.mkdir("test_folder")
    print("\n' test_folder' create kar diya!")
except FileExistsError:
    print("\n' test_folder' already exist karti hai!")