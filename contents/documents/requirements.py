import subprocess


with open('requirements1.txt', 'w') as file:
    subprocess.run(['pip', 'freeze'], stdout=file)
