
import os
from sys import argv

def cleanUp():
    """Looks in startPath for all filenames containing argv[1], creates and
    moves them to a sub-directory with the same name."""
    startPath = #Path of directory you'd like to clean up.
    targetPath = os.path.join(startPath, argv[1])
    print(targetPath)

    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

    for filename in os.listdir(startPath):
        #Change the extension to whatver type of file you'd like to clean up.
        if argv[1] in filename and filename.endswith('.jpg'):
            currentLoc = os.path.join(startPath, filename)
            targetLoc = os.path.join(targetPath, filename)
            os.rename(currentLoc, targetLoc)
            print(filename)

def main():
    cleanUp()

in __name__ == '__main__':
    main()
