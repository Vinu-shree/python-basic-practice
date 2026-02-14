# Basic file handling in python
# Internship - File Handling

## writing to a file
with open("sample.txt","w")as file:
    file.write("Hello, this is my internship practice.\n")
    file.write("Learning File Handling in Python.\n")
print("Data written successfully.")

# Reading from the file
with open("sample.txt","r")as file:
    content=file.read()
print("File content:")
print(content)