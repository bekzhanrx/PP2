import os

if os.path.exists('ex.txt'):
    os.remove('ex.txt')
else:
    print("Such file does not exist!")
