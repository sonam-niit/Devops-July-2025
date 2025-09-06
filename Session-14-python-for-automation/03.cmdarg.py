import sys

print("Script name: ",sys.argv[0])
print("Arguments: ",sys.argv[1:])

# command to execute
# py 03.cmdarg.py file1.txt file2.txt hello sonam

# iterate using for loop
for i in sys.argv[1:]:
    print(i)


