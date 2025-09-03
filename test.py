import subprocess
# import os
cmdc= "dir"
result= subprocess.run(["cmd", "/c", cmdc], capture_output=True, text=True )
print(result.stdout)
for i in range(4):
    a=input("enter the command:")
    b=subprocess.run(["cmd", "/c", a], capture_output=True, text=True)
    print(b.stdout)
# result= subprocess.Popen(["ping","192.168.29.172"], stdout=subprocess.PIPE, text=True)
# for line in result.stdout:
#     print(line.strip())


