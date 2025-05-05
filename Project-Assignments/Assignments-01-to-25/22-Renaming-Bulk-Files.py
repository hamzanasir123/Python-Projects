import os

def main():
    i = 0
    print("This program will rename all the files(Images) in the given directory.")
    print("Please make sure that the directory contains only the files you want to rename.")
    print("The files will be renamed as img0.jpg, img1.jpg, img2.jpg, and so on.")
    print("Please enter / on the end of the path. And make sure to use / instead of \ in the path.")
    print("For example: C:/Users/Username/Desktop/")
    path = input("Enter the path of the file: ")

    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

    else:
        print("All files have been renamed successfully.")



if __name__ == '__main__':
    main()
