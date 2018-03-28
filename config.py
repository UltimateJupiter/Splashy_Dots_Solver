import os
if os.name == 'posix':
    os.system('sudo apt-get install python-pip')
    os.system('sudo pip install scikit-image')
    os.system('sudo pip install numpy')
    os.system('sudo pip install matplotlib')
    os.system('sudo apt-get install python-tk')
