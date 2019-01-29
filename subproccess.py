import os
import subprocess

cmd = "ls -l"

return_value = os.system(cmd)
#print(return_value)

if return_value == 0:
    print('success')
 #   os.mkdir('test')
    os.system(cmd)
else:
    print('fail')

print("Enter Checking git version")
chk_ver = input("Do you want to check the version :- ")
if chk_ver == 'y':
    cmd = "git --version"
    return_value = subprocess.call(cmd, shell=True)
    print(return_value)
else:
    print("fail")



