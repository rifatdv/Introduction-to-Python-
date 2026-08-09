try:
    # Create and write to a file
    file = open("file1.txt", "w")
    file.write("Hi there.\n")
    file.write("This is Programming In Python Course.\n")
    file.close()

    # Read the file
    file = open("file1.txt", "r")
    content = file.read()
    print("File content:")
    print(content)
    file.close()

    # Append new content to the file
    file = open("file1.txt", "a")
    file.write("This course based on basics of python.\n")
    file.close()

    # Read again after appending
    file = open("file1.txt", "r")
    print("Updated file content:")
    print(file.read())
    file.close()

    # Create a new file
    file = open("newfile.txt", "x")
    file.write("This is a newly created file.")
    file.close()

    print("Files created and modified successfully.")

except FileExistsError:
    print("Error: The file already exists.")

except FileNotFoundError:
    print("Error: File or directory not found.")

except PermissionError:
    print("Error: You do not have permission to access the file.")

except Exception as e:
    print("Unexpected error:", e)