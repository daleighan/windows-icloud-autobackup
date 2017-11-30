# This script will move unmoved items from the doucuments and download folders to the icloud folder

import os

def backup():
    files = os.listdir('/')
    print(files)

if __name__ == "__main__":
    print("Backing up files to icloud")
    backup()
    print("Backup complete")
