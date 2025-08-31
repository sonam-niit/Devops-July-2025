import shutil

total,used,free=shutil.disk_usage('/')
print(f"Total: {total//(2**30)} GB")
print(f"Used: {used//(2**30)} GB")
print(f"Free: {free//(2**30)} GB")

#percentage Usage
percentage_used=(used/total) *100
print(f"Disk Usage {percentage_used:.2f}%")