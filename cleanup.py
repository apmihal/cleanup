
import os
from sys import argv

def cleanUp():
    """Looks in startPath for all filenames containing argv[1], creates and
    moves them to a sub-directory with the same name."""
    if len(argv) != 2:
        print("Use: specify the string you'd like to search for in filenames as a command line argument.")
        return 1

    startPath = 'C:/Users/AndrewM/Desktop/Projects/LC101/test'
    #Path of directory you'd like to clean up.
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

if __name__ == '__main__':
    main()
