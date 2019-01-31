import os
import time

print(100 * "=")
print("Installing Updates")
print(100 * "=")


update = "sudo apt-get update -y && sudo apt-get upgrade -y"
os.system(update)

print(100 * "=")
print("Editing Host file")
print(100 * "=")

log = open("/etc/hostname", "w")
log.write("db-manager")

print(100 * "=")
print("Adding the mongo key")
print(100 * "=")
mongo_key = "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4"
os.system(mongo_key)

print(100 * "=")
print("Adding the mongo repository")
print(100 * "=")
mongo_repo = 'echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list'
os.system(mongo_repo)

os.system(update)

print(100 * "=")
print("Installing MongoDB")
print(100 * "=")
mongo_pkg = "sudo apt-get install -y mongodb-org"
os.system(mongo_pkg)

print("Starting and Enabling Mongo")

service_start = "sudo systemctl start mongod && sudo systemctl enable mongod"
os.system(service_start)

print("Checking Ports")
time.sleep(10)
print(os.system("netstat -tlnp"))