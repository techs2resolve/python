

software = ['sudo apt-get install apache2 php mysql-server phpmyadmin -y',
            'sudo apt-get install filezilla vim -y',
            'wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -',
            'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list',
            'sudo apt-get update','sudo apt-get install sublime-text -y']



i = 0
for i in range(len(software)):
    print(software[i])
    i += 1

