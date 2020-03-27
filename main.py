import numpy as np
import cv2 
import argparse
import matplotlib.pyplot as plt

SIZE = 8
path = ""

def fill_rect(r, c, k, val):
#This function will fill rectangle of SIZE * SIZE with given value
    for i in range(r, r + SIZE):
        for j in range(c, c + SIZE):
            img[i][j][k] = val

def convert():
#This function will iterate each SIZEth Pixel
    print('Now Converting Image...')
    for i in range(0, row - SIZE, SIZE):
        for j in range(0, col - SIZE, SIZE):
            for k in range(DEPTH):
                fill_rect(i, j, k, img[i][j][k])

if __name__ == "__main__":
#Parser for parsing command line arguments.
    parser = argparse.ArgumentParser(description = "This is a simple python program to pixelate provided image.")
    parser.add_argument('file', action = "store", help = 'Path of the input image.') 
    parser.add_argument('-size', action = "store", default = 8, type = int, help = 'SIZE (Intensity) of pixeling.')
    parser.add_argument('-grey', action = "store_true", default = False, help = 'Option to convert an image to greyscale.')
    args = parser.parse_args() 
    
    path = args.file
    img = cv2.imread(path)
    img  = np.asarray(img)
    row = img.shape[0]
    col = img.shape[1]
    DEPTH = img.shape[2]
    print('Recieved Image with Shape:',img.shape)
    
    SIZE = args.size
    
    if(args.grey):
    #This converts image to greyscale
        print('Converting Image to greyscale (if it is not already greyscale)...')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.reshape(img, (img.shape[0], img.shape[1], 1))
        DEPTH = 1
        print('Now shape of the Image is:',img.shape)
    
    convert()
    
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.plot()
    plt.show()
    choice = input('Save ? <y/n>: ')
    if(choice =="Y" or choice == "y"):
        plt.imsave(input('Enter Name for for file: ')+'.jpg', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))