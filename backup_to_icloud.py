# This script will move unmoved items from the doucuments and download folders to the icloud folder

import os
from shutil import copytree

def backup():
    documents_files = os.listdir('/users/leighn/Documents')
    icloud_files_documents = os.listdir('/users/leighn/iCloudDrive/Documents')
    # This section backs up the documents folder
    
    documents_to_add = []

    for file in documents_files:
        if file not in icloud_files_documents:
            documents_to_add.append(file)

    for file_name in documents_to_add:
        try:
            copytree('/users/leighn/Documents/' + file_name, '/users/leighn/iCloudDrive/Documents/' + file_name)
            print(file_name)
        except:
            print('Permission denied')

    
    downloads_files = os.listdir('/users/leighn/Downloads')
    icloud_files_downloads = os.listdir('/users/leighn/iCloudDrive/Downloads')

    downloads_to_add = []

    for file in downloads_files:
        if file not in icloud_files_downloads:
            downloads_to_add.append(file)

    for file_name in downloads_to_add:
        try:
            copytree('/users/leighn/Downloads/' + file_name, '/users/leighn/iCloudDrive/Downloads/' + file_name)
            print(file_name)
        except:
            print('file not copied', file_name)

if __name__ == "__main__":
    print("Backing up files to icloud")
    backup()
    print("Backup complete")
