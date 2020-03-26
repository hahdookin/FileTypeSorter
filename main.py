"""
 - read through a directory (listdir)
 - somehow lists out all the files (list comprehension)
 - create folders based on the files extension (mkdir)
 - move files into the directory of its type (rename)
 - complete this process while the directory has files (while)
 - add event listener to add files dynamically
"""

from os import listdir, rename, mkdir, path, environ
from os.path import isfile, join

grouped_exts = {
    'images': ['png', 'jpeg', 'jpg', 'gif', 'jpeg_large', 'jpg_large'],
    'videos': ['mp4', 'webm', 'vlc', 'avi', 'wmv', 'mkv', 'flv'],
    'audio': ['mp3', 'wav', 'm4p', 'm4a'],
    'zips': ['rar', 'zip', '7z', 'gz'],
    'office': ['ppt', 'pptx', 'doc', 'docx', 'xlsx']
}

# Path goes here
if environ['COMPUTERNAME'] == 'CHRIS':
    myPath = r'F:\Users\Chris\Documents\Archives\Downloads\\'
elif environ['COMPUTERNAME'] == 'LAPTOP-GGAAAEHH':
    myPath = r'C:\Users\Chris\Downloads\\'

onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
onlyFolders = [f for f in listdir(myPath) if not isfile(join(myPath, f))]


for file in onlyFiles:
    original_ext = str(file.split(".")[-1]).lower()
    original_file = file
    ext = str(file.split(".")[-1]).lower()

    for group, exts in grouped_exts.items():
        if ext in exts:
            ext = group

    # make directory if isn't there
    if ext not in onlyFolders:
        mkdir(myPath + ext)
        print(ext + " folder created")
        onlyFolders.append(ext)

    # Check if filename already exists
    i = 1
    while path.exists(myPath + ext + r'\\' + file):
        # print(file)
        file = f"{original_file.replace('.' + original_ext, f'[{i}].' + original_ext)}"
        i += 1

    print(file + " => " + ext)
    # put the file in the appropriate directory
    rename(myPath + original_file, myPath + ext + r'\\' + file)



