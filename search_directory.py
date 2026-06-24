import os
import sys

def initialization():
    start = input("Enter the directory to search: ")
    search = input("Enter the word you are looking for: ")

    if not start.strip() or not search.strip():
        print("Error: Inputs cannot be empty. Please try again.\n")
        sys.exit()  # Exit
    if not os.path.exists(start) or not os.path.isdir(start):
        print("Error: Invalid directory path. Please try again.\n")
        sys.exit()
    return start, search

# D:\Python\Levi9\Week 1\Temperature Logger

start_dir, search_word = initialization()

for root, dirs, files in os.walk(start_dir):
    for file in files:
        full_path = os.path.join(root, file)
        if search_word.lower() in file.lower():
            print(full_path)
