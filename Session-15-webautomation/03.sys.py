import sys

print("Python version", sys.version)
print("Python Executable", sys.executable)
print("System Platform", sys.platform)
# print("Module Search path", sys.path)

print("file name",sys.argv[0]) # CLI

#exit program
# sys.exit(0)

sys.stderr.write("This is Standard error")