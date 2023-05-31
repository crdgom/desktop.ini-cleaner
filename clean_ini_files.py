import os
import threading
import time

global files, number_files, found, deleted, stop

files = []
number_files = 0
found = 0
deleted = 0
stop = False
    
def menu_actions():
    while stop == False:
        print(f'Scanning.', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Scanning..', end='\r')        
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Scanning...', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')

def search_for_files(path, searched_file):
    
    global files, number_files, found, stop

    for (dirpath, dirnames, filenames) in os.walk(path):        
        for file in filenames:
            if file == searched_file:
                files.append({"path": dirpath,
                              "file": file})
                found = found + 1
        number_files = number_files + len(filenames)

    stop = True

def confirm_delete():

    global files, deleted

    print(f'>>> Will be removed {found} files.')
    print(f'>>> Type "Yes" to confirm the deletion of the files')

    confirmation = input()

    if confirmation != 'Yes':
        print(f'>>> Cancelled operation!')

    else:
        for file in files:
            full_file = file["path"] + '/' + file["file"]
            os.remove(full_file)
            print(f'>>> Total number of deleted files: { full_file }')
            deleted = deleted + 1

    print(f'>>> Deleted files: { deleted }')    

print('\n>>> This program searches for files by name to delete them. \n>>> Use it very carefully, the files will be deleted \n>>> and this action cannot be undone. \n\n')        
print('>>> Which directory do you want to scan?')

directory = input('>>> Please enter the complete path e.g.: C:\\User\\Desktop\\SomeDir\n')

print('>>> What is the filename?')

filename = input('>>> Please enter the file name and file extension, e.g. desktop.ini\n')

threading.Thread(target=menu_actions).start()

search_for_files(directory, filename)

print(f'>>> Total files scanned: { number_files }')

if len(files) > 0:
    confirm_delete()
else:
    print(f'>>> No files found!')
