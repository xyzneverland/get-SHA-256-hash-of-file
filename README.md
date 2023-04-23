# get-SHA-256-hash-of-file
The purpose of this script is to calculate the SHA-256 hash value of a specified file and print it to the console. The script first prompts the user to enter the file name and checks if the file exists in the current directory. If the file is found, the script reads the contents of the file using the read_file() function and calculates its SHA-256 hash value. Finally, the script prints the hash value to the console and waits for 10 seconds before closing.

This script is useful for verifying the integrity of a file. The SHA-256 hash value of a file is unique and can be used to check if the contents of the file have been modified or corrupted in any way. By calculating the SHA-256 hash value of the file and comparing it to a known good hash, you can be sure that the file has not been tampered with.

To use this script, you need to have Python installed on your computer. You can download and install the latest version of Python from the official website.

To run the script, open a terminal or command prompt, navigate to the directory where the script is located, and run the command "python get-SHA-256-hash-of-file.py". The script will then prompt you to enter the file name. If the file is found, the script will calculate the SHA-256 hash value of the file and print it to the console.

The script works by first importing the necessary modules, including hashlib, os, and time. The hashlib module is used to calculate the SHA-256 hash value of the file, the os module is used to search for the file, and the time module is used to pause the script before closing the window.

The script defines the read_file() function, which is used to read the contents of the file in binary mode. The function takes the file name as a parameter, opens the file in binary read mode, reads the contents of the file, and returns the binary data.

Next, the script prompts the user to enter the file name and uses a while loop to search for the file using the os.path.exists() method. If the file is found, the script calls the read_file() function to read the contents of the file as binary data.

The script then creates a new hashlib.sha256 object, which is used to calculate the SHA-256 hash value of the file. The binary data is passed to the sha256.update() method, which updates the hash value with the contents of the file. The resulting SHA-256 hash value is stored in the file_hash variable.

Finally, the script prints the SHA-256 hash value of the file to the console using an f-string. The script then waits for 10 seconds using the time.sleep() method before closing the window.

It is important to note that the script can only find the file if it is located in the same directory as the script, or if you provide the complete file path when prompted.
