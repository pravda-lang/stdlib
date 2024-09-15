import subprocess

def main(command):
    if isinstance(command, list):
        subprocess.run(" ".join(command), shell=True)
    else:
        subprocess.run(command, shell=True)
