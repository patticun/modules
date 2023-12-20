# file_operations.py

import os
import shutil

def copy_file(source_path, destination_path):
     """Copying a file from one location to another."""
     try:
         shutil.copy2(source_path, destination_path)
         print(f"File copied from {source_path} to {destination_path}")
     except FileNotFoundError:
         print("Error: The specified file was not found")

def move_file(source_path, destination_path):
     """Move a file from one location to another."""
     try:
         shutil.move(source_path, destination_path)
         print(f"File moved from {source_path} to {destination_path}")
     except FileNotFoundError:
         print("Error: The specified file was not found")

def delete_file(file_path):
     """Deleting a file."""
     try:
         os.remove(file_path)
         print(f"File deleted: {file_path}")
     except FileNotFoundError:
         print("Error: The specified file was not found")
     except PermissionError:
         print("Error: No permission to delete file")
