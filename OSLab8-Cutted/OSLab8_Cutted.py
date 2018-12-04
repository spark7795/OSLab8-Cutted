# Уровень вложенности через подсчет слешей
import win32con
import win32api
import os

# limits for recursive walking
lower_limit = 2
upper_limit = 4
# Only one file extension should be used
file_extension = 'docx'
go_dir = input('Input dir name:')
folder = []
FileList= []
for i in os.walk(go_dir):
    folder.append(i)
# all files
print('=== Show only <' + file_extension + '> hidden files in walking limit ===')
for address, dirs, files in folder:
    for file in files:
        if win32api.GetFileAttributes(address+'/'+file) & win32con.FILE_ATTRIBUTE_HIDDEN:
            if ((address.count('\\')+1) >= lower_limit) & ((address.count('\\')+1) <= upper_limit):
                if file.endswith('.'+file_extension):
                    print(address+'/'+file)
                    FileList.append(file)
print ('=== File names: ===')
print ('Unsorted alphabeticaly: \n' + str(FileList))
FileList.sort()
print ('Sorted alphabeticaly: \n' + str(FileList))