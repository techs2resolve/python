import datetime
import pyautogui
import fnmatch
import os
import time

while True:
    now = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    screenshot = pyautogui.screenshot(now+'.png')
    time.sleep(60)

# for file in os.listdir():
#     if fnmatch.fnmatch(file, '*.png'):
#         print(file)



#for files in os.listdir():
 #   print(files)


# For python 2.7
# sudo apt-get install python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev
# sudo apt-get install python-xlib
#sudo apt-get install scrot -y
# sudo python -m pip install pyautogui
# export LC_CTYPE=en_US.UTF-8
# sudo pip install pyautogui
# export DISPLAY=:0



# sudo apt-get install python3-xlib -y
# sudo apt-get install python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev -y
# sudo apt-get install scrot -y
# export LC_CTYPE=en_US.UTF-8
# sudo python3 -m pip install pyautogui
# export DISPLAY=:0
