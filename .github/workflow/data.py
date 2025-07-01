with open("sai.py", "w") as file:
    file.write("Python is good!")
with open("sai.py", "r") as file:
    content = file.read()
    print("File Content After Writing:", content)
with open("sai.py", "a") as file:
    file.write("\nLearning file handling.")  
with open("sai.py", "r") as file:
    updated_content = file.read()
    print("\nFile Content After Appending", updated_content) 
try:
    with open("missing.txt", "r") as file:
        content = file.read
        print(content)
except FileNotFoundError:
    print("Error: The file 'missing.txt' does not exist!")
try:
    with open("sai.py", "r") as file:
        content = file.read
except PermissionError:
    print("Error: you don't have permission to access this file!")
try:
    file = open("sai.py", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: You dont't have permission to access this file!")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed successfully!") 



