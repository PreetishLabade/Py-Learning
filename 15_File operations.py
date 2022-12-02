"""File read modes
"r" - for reading -default
"t" - text mode -default
"w" - for writing
"x" - create file if not exists
"a" - append content to file
"b" - binary mode
"r+" - read and write
"""

# Create a file
# file = open("file1.txt, "x")

# Read a file
file = open("file1.txt", "rt")
content = file.read()
# file1.txt is open and stored in a variable file. This variable file is called file pointer .
# Once we read contents of file, then this pointer becomes empty
print(content)
file.close()

# Read a file in binary
file = open("file1.txt", "rb")
content = file.read()
print(content)

# Readline function
file = open("file1.txt", "rt")
print(file.readline())
# Readline reads first line by default

# Readlines create a list of each line of file
print(file.readlines())

file.close()

# Append content to a file
file = open("file1.txt", "a")
file.write("Sample line\n")

# Read and write mode together
file = open("file1.txt", "r+")
content = file.read()
print(content)
file.write("Sample file written with r+ mode")

# To see current file pointer location
print(file.tell())

# To set file pointer location
file.seek(20)
file.close()