# This script will move unmoved items from the doucuments and download folders to the icloud folder

import os
from shutil import copytree, copyfile
import time

def backup():
   
    # This section backs up the documents folder
    documents_dirs_n_files = []
    icloud_dirs_n_files =[]
    
    for root, directories, filenames in os.walk('/users/leighn/Documents'):
        for directory in directories:
            documents_dirs_n_files.append(os.path.join(root, directory)[24:])
        for filename in filenames:
             documents_dirs_n_files.append(os.path.join(root ,filename)[24:])

    for root, directories, filenames in os.walk('/users/leighn/iCloudDrive/Documents'):
        for directory in directories:
            icloud_dirs_n_files.append(os.path.join(root, directory)[36:])
        for filename in filenames:
             icloud_dirs_n_files.append(os.path.join(root ,filename)[36:])

    documents_to_add = []
    
    for file in documents_dirs_n_files:
        if file not in icloud_dirs_n_files:
            documents_to_add.append(file)

    documents_to_remove = []

    for file in icloud_dirs_n_files:
        if file not in documents_dirs_n_files:
            documents_to_remove.append(file)
    
    for file_name in documents_to_add:
        try:
            if file_name != "My Music" and file_name != "My Pictures" and file_name != "My Videos":
                copytree('/users/leighn/Documents/' + file_name, '/users/leighn/iCloudDrive/Documents/' + file_name)
                print('folder copied', file_name)
        except:
            try:
                copyfile('/users/leighn/Documents/' + file_name, '/users/leighn/iCloudDrive/Documents/' + file_name)
                print('file copied', file_name)
            except:
                print('error on:', file_name)
                
    for file_name in documents_to_remove:
        try:
            rmtree('/users/leighn/iCloudDrive/Documents/' + file_name, ignore_errors=True)
            print('folder removed', file_name)
        except:
            try:
                os.remove('/users/leighn/iCloudDrive/Documents/' + file_name)
                print('file removed', file_name)
            except:
                try:
                    os.rmdir('/users/leighn/iCloudDrive/Documents/' + file_name)
                except:
                    print('removal of', file_name, 'failed')
                
                
    # This section backs up the downloads folder 
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
            try:
                copyfile('/users/leighn/Downloads/' + file_name, '/users/leighn/iCloudDrive/Downloads/' + file_name)
                print(file_name)
            except:
                print('copying failed for', file_name)

if __name__ == "__main__":
    start_time = time.time()
    print("Backing up files to icloud folder")
    backup()
    finish_time = time.time()
    print("Backup complete")
    print("Time elapesed:", finish_time - start_time, "seconds")
