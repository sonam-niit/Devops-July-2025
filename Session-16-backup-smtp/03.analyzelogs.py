import re
with open("app.log") as f:
    for line in f:
        if "ERROR" in line or "CRITICAL" in line:
            print(line.strip())
            
pattern = re.compile(r'.* - (ERROR|CRITICAL) - *')
with open("app.log") as f:
    for line in f:
        if pattern.match(line):
            print(line.strip())
            