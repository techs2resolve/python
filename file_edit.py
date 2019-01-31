import os

#Checking OS version

os_version = "cat /etc/issue"
print(f"Your OS version is {os.system(os_version)}")

print("Updating the system")
update = "sudo apt-get update -y && sudo apt-get upgrade -y"
os.system(update)

log = open("/Users/sarfaraz/linux-skills.txt", "w")
log.write("192.168.15.150 db-manager")
view = "cat /Users/sarfaraz/linux-skills.txt "
print(os.system(viewm))
