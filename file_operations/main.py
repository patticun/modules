#main.py

import file_operations

# Create test files
with open("test_file.txt", "w") as file:
     file.write("Hello, this is a test file.")

# Use functions from the module to copy, move and delete files
file_operations.copy_file("test_file.txt", "copy_of_test_file.txt")
file_operations.move_file("test_file.txt", "moved_test_file.txt")
file_operations.delete_file("copy_of_test_file.txt")
