import subprocess

subprocess.run(["echo","Hello From Subprocess"])
# run command in shell

result=subprocess.run(["ls","-l"],capture_output=True,text=True)
print("STDOut:",result.stdout)
print("STDErr:",result.stderr)
