#!/usr/bin/python3
# SHA-256 hash of the file v1.0 (https://github.com/xyzneverland/get-SHA-256-hash-of-file/)
# by xyzneverland (https://github.com/xyzneverland/)
import hashlib
import os
import time

def read_file(file_name):
  with open(file_name, "rb") as f:
    return f.read()

file_name = input("Please enter the file name: ")

while not os.path.exists(file_name):
  file_name = input("File not found. Please enter the file name again: ")

file_contents = read_file(file_name)
sha256 = hashlib.sha256()
sha256.update(file_contents)
file_hash = sha256.hexdigest()

print(f"The SHA-256 hash of the file '{file_name}' is: {file_hash}")
time.sleep(10)
