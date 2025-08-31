import os
import platform as pt

current_directory=os.getcwd()
print(f"Curruent Working Directory: {current_directory}")
print("Curruent Working Directory:",current_directory)

print(f"CPU Count: {os.cpu_count()}")
print(f"Current Directory {os.curdir}")

print(f"Architecture {pt.architecture()}")
print(f" {pt.python_version()}")