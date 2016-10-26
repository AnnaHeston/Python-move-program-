import shutil
import os

def main():
    source ='C:\\Users\\Anna\\Desktop\\FolderA\\'
    destination ='C:\\Users\\Anna\\Desktop\\FolderB\\'
    move_Files(source, destination)

def move_Files(source, destination):
    for files in os.listdir(source):
        if files.endswith(".txt"):
            shutil.move(source + files,destination)
            print (destination + files)
        


if __name__ == "__main__":
    main()
