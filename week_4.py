import os


def file_handling (file):
    files = open(file, "rt")
    fil = open("updated_file.txt", "w")
    fil.write(files.read())


    fil.close()
    files.close()
    fil = open("updated_file.txt", "rt")
    finals = fil.read()

    return finals
file = input("Enter a file name with text or the path the path: ")

if os.path.exists(file):
    print(file_handling(file))
else:
    print("The file inputted is not valid or incorrect path given")

