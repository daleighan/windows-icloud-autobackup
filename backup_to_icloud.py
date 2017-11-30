# This script will move unmoved items from the doucuments and download folders to the icloud folder

import os
from shutil import copyfile

def backup():
    documents_files = os.listdir('/users/leighn/Documents')
    #print(files)
    icloud_files_documents = os.listdir('/users/leighn/iCloudDrive/Documents')
    documents_to_add = []
    print(documents_to_add)
    print(documents_to_add)

    for file in documents_files:
        if file not in icloud_files_documents:
            documents_to_add.append(file)

    for file_name in documents_to_add:
        try:
            copyfile('/users/leighn/Documents/' + file_name, '/users/leighn/iCloudDrive/Documents/' + file_name)
            print(file_name)
        except:
            print('Permission denied')

if __name__ == "__main__":
    print("Backing up files to icloud")
    backup()
    print("Backup complete")
