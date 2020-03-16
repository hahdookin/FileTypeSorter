"""
 - read through a directory (listdir)
 - somehow lists out all the files (list comprehension)
 - create folders based on the files extension (mkdir)
 - move files into the directory of its type (rename)
 - complete this process while the directory has files (while)
 - add event listener to add files dynamically
"""

from os import listdir, rename, mkdir
from os.path import isfile, join

grouped_exts = {
    'images': ['png', 'jpeg', 'jpg', 'gif', 'jpeg_large', 'jpg_large'],
    'videos': ['mp4', 'webm', 'vlc', 'avi', 'wmv', 'mkv', 'flv'],
    'audio': ['mp3', 'wav', 'm4p', 'm4a'],
    'zips': ['rar', 'zip', '7z', 'gz'],
    'office': ['ppt', 'pptx', 'doc', 'docx', 'xlsx']
}

# Path goes here
myPath = r'F:\Users\Chris\Documents\Archives\Downloads\\'

onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
onlyFolders = [f for f in listdir(myPath) if not isfile(join(myPath, f))]


for file in onlyFiles:
    ext = str(file.split(".")[-1]).lower()

    for group, exts in grouped_exts.items():
        if ext in exts:
            ext = group

    # make directory if isn't there
    if ext not in onlyFolders:
        mkdir(myPath + ext)
        print(ext + " folder created")
        onlyFolders.append(ext)

    print(file + " => " + ext)
    # put the file in the appropriate directory
    rename(myPath + file, myPath + ext + r'\\' + file)



