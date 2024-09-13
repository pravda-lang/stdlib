import subprocess

def main(command):
    return subprocess.run(command, shell = True, text = True,  stdout = subprocess.PIPE).stdout
