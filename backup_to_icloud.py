# This script will move unmoved items from the doucuments and download folders to the icloud folder

import os

def backup():
    documents_files = os.listdir('/users/leighn/Documents')
    #print(files)
    icloud_files_documents = os.listdir('/users/leighn/iCloudDrive/Documents')
    documents_to_add = []

    for file in documents_files:
        if file not in icloud_files_documents:
            documents_to_add.append(file)

    print(documents_to_add)


if __name__ == "__main__":
    print("Backing up files to icloud")
    backup()
    print("Backup complete")
