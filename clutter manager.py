import os
import shutil


def makeFolder(foldername):
    """function to make folder if not exists"""
    if not os.path.exists(foldername):
        os.mkdir(foldername)


def separateFiles(catagoryName, extensions):
    """function to separate file by thier extensions and store them in an array"""
    catagoryName = [catagoryName for catagoryName in files if
                    str(catagoryName).lower().endswith(extensions)]
    return catagoryName


def moveFilesToFolder(files, foldername):
    """function to move files in folder"""
    for file in files:
        shutil.move(file, foldername)


if __name__ == '__main__':

    clean = False

    # taking path input from the user
    path = input("Enter path or c for choose current directory: ")

    # cheking user entered path exits or not
    if path != "c":
        try:
            # if path exits change path using os module and clean dir
            os.chdir(path)
            clean = True
        except:
            # if path doesn't exits throw error
            print("Invalid Path!")
            clean = False

    elif path == "c":
        clean = True

    if clean:
        # listing of files in present directory
        files = os.listdir()

        # making folders if not exists
        makeFolder("Images")
        makeFolder("Videos")
        makeFolder("Music")
        makeFolder("Documents")

        # seprating files according to extensions
        images = separateFiles("images", (".png", ".jpg", ".jpeg"))
        videos = separateFiles("videos", (".mp4", ".mkv", ".3gp", ".avi"))
        musics = separateFiles("musics", (".mp3", ".wave", ".mp4a", ".m4a"))
        docs = separateFiles("docs", (".pdf", ".txt", ".doc", ".zip", ".rar"))

        # moving files in folders
        moveFilesToFolder(images, "Images")
        moveFilesToFolder(videos, "Videos")
        moveFilesToFolder(musics, "Music")
        moveFilesToFolder(docs, "Documents")
