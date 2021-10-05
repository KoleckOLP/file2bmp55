import os, sys
from PIL import Image
from math import sqrt, ceil


def Fatui(inputFilePath: str, outputFilePath: str):
    inputFile = open(inputFilePath, "rb").read()  # reads bytes from a file to bytes

    inputFile = list(inputFile)  # converts bytes to array

    width = ceil(sqrt(len(inputFile)))  # counts the width so the output image can be a square, of course not a float number

    inputFile = [
        inputFile[i * width:(i * width) + width]
        for i in range(ceil(len(inputFile) / width))
    ]  # turns our byte array to a 2D array

    height = len(inputFile)

    if (len(inputFile[0]) > len(inputFile[height - 1])):
        missing = len(inputFile[0]) - len(inputFile[height - 1])
        zeros = [0] * missing
        inputFile[height - 1].extend(zeros)  # adds zero padding if last array is shorter

    img = Image.new('P', (height, width), 0)  # this normally makes a grayscale image
    img.putpalette([
        0, 0, 0,
        128, 0, 0,
        0, 128, 0,
        128, 128, 0,
        0, 0, 128,
        128, 0, 128,
        0, 128, 128,
        192, 192, 192,
        128, 128, 128,
        255, 0, 0,
        0, 255, 0,
        255, 255, 0,
        0, 0, 255,
        255, 0, 255,
        0, 255, 255,
        255, 255, 255,
        0, 0, 0,
        0, 0, 95,
        0, 0, 135,
        0, 0, 175,
        0, 0, 215,
        0, 0, 255,
        0, 95, 0,
        0, 95, 95,
        0, 95, 135,
        0, 95, 175,
        0, 95, 215,
        0, 95, 255,
        0, 135, 0,
        0, 135, 95,
        0, 135, 135,
        0, 135, 175,
        0, 135, 215,
        0, 135, 255,
        0, 175, 0,
        0, 175, 95,
        0, 175, 135,
        0, 175, 175,
        0, 175, 215,
        0, 175, 255,
        0, 215, 0,
        0, 215, 95,
        0, 215, 135,
        0, 215, 175,
        0, 215, 215,
        0, 215, 255,
        0, 255, 0,
        0, 255, 95,
        0, 255, 135,
        0, 255, 175,
        0, 255, 215,
        0, 255, 255,
        95, 0, 0,
        95, 0, 95,
        95, 0, 135,
        95, 0, 175,
        95, 0, 215,
        95, 0, 255,
        95, 95, 0,
        95, 95, 95,
        95, 95, 135,
        95, 95, 175,
        95, 95, 215,
        95, 95, 255,
        95, 135, 0,
        95, 135, 95,
        95, 135, 135,
        95, 135, 175,
        95, 135, 215,
        95, 135, 255,
        95, 175, 0,
        95, 175, 95,
        95, 175, 135,
        95, 175, 175,
        95, 175, 215,
        95, 175, 255,
        95, 215, 0,
        95, 215, 95,
        95, 215, 135,
        95, 215, 175,
        95, 215, 215,
        95, 215, 255,
        95, 255, 0,
        95, 255, 95,
        95, 255, 135,
        95, 255, 175,
        95, 255, 215,
        95, 255, 255,
        135, 0, 0,
        135, 0, 95,
        135, 0, 135,
        135, 0, 175,
        135, 0, 215,
        135, 0, 255,
        135, 95, 0,
        135, 95, 95,
        135, 95, 135,
        135, 95, 175,
        135, 95, 215,
        135, 95, 255,
        135, 135, 0,
        135, 135, 95,
        135, 135, 135,
        135, 135, 175,
        135, 135, 215,
        135, 135, 255,
        135, 175, 0,
        135, 175, 95,
        135, 175, 135,
        135, 175, 175,
        135, 175, 215,
        135, 175, 255,
        135, 215, 0,
        135, 215, 95,
        135, 215, 135,
        135, 215, 175,
        135, 215, 215,
        135, 215, 255,
        135, 255, 0,
        135, 255, 95,
        135, 255, 135,
        135, 255, 175,
        135, 255, 215,
        135, 255, 255,
        175, 0, 0,
        175, 0, 95,
        175, 0, 135,
        175, 0, 175,
        175, 0, 215,
        175, 0, 255,
        175, 95, 0,
        175, 95, 95,
        175, 95, 135,
        175, 95, 175,
        175, 95, 215,
        175, 95, 255,
        175, 135, 0,
        175, 135, 95,
        175, 135, 135,
        175, 135, 175,
        175, 135, 215,
        175, 135, 255,
        175, 175, 0,
        175, 175, 95,
        175, 175, 135,
        175, 175, 175,
        175, 175, 215,
        175, 175, 255,
        175, 215, 0,
        175, 215, 95,
        175, 215, 135,
        175, 215, 175,
        175, 215, 215,
        175, 215, 255,
        175, 255, 0,
        175, 255, 95,
        175, 255, 135,
        175, 255, 175,
        175, 255, 215,
        175, 255, 255,
        215, 0, 0,
        215, 0, 95,
        215, 0, 135,
        215, 0, 175,
        215, 0, 215,
        215, 0, 255,
        215, 95, 0,
        215, 95, 95,
        215, 95, 135,
        215, 95, 175,
        215, 95, 215,
        215, 95, 255,
        215, 135, 0,
        215, 135, 95,
        215, 135, 135,
        215, 135, 175,
        215, 135, 215,
        215, 135, 255,
        215, 175, 0,
        215, 175, 95,
        215, 175, 135,
        215, 175, 175,
        215, 175, 215,
        215, 175, 255,
        215, 215, 0,
        215, 215, 95,
        215, 215, 135,
        215, 215, 175,
        215, 215, 215,
        215, 215, 255,
        215, 255, 0,
        215, 255, 95,
        215, 255, 135,
        215, 255, 175,
        215, 255, 215,
        215, 255, 255,
        255, 0, 0,
        255, 0, 95,
        255, 0, 135,
        255, 0, 175,
        255, 0, 215,
        255, 0, 255,
        255, 95, 0,
        255, 95, 95,
        255, 95, 135,
        255, 95, 175,
        255, 95, 215,
        255, 95, 255,
        255, 135, 0,
        255, 135, 95,
        255, 135, 135,
        255, 135, 175,
        255, 135, 215,
        255, 135, 255,
        255, 175, 0,
        255, 175, 95,
        255, 175, 135,
        255, 175, 175,
        255, 175, 215,
        255, 175, 255,
        255, 215, 0,
        255, 215, 95,
        255, 215, 135,
        255, 215, 175,
        255, 215, 215,
        255, 215, 255,
        255, 255, 0,
        255, 255, 95,
        255, 255, 135,
        255, 255, 175,
        255, 255, 215,
        255, 255, 255,
        8, 8, 8,
        18, 18, 18,
        28, 28, 28,
        38, 38, 38,
        48, 48, 48,
        58, 58, 58,
        68, 68, 68,
        78, 78, 78,
        88, 88, 88,
        98, 98, 98,
        108, 108, 108,
        118, 118, 118,
        128, 128, 128,
        138, 138, 138,
        148, 148, 148,
        158, 158, 158,
        168, 168, 168,
        178, 178, 178,
        188, 188, 188,
        198, 198, 198,
        208, 208, 208,
        218, 218, 218,
        228, 228, 228,
        238, 238, 238,
    ])  # this palette adds colors (probably Xterm 255 color palette, I do not remember)
    pixels = img.load()  # no idea what this does

    for i in range(img.size[0]):  # loops through my 2D array of bytes and writes them as pixels
        for j in range(img.size[1]):
            pixels[i, j] = inputFile[i][j]

    os.makedirs(os.path.dirname(os.path.realpath(outputFilePath)), exist_ok=True)  # creates directories if necessary

    img.save(outputFilePath)  # saves image

    Image.open(outputFilePath).save(outputFilePath[:-3]+"png")  # converting to a png


def ImToFile(inputFilePath: str):
    Image.open(inputFilePath).save(inputFilePath[:-3] + "bmp")  # converting to a bmp


if len(sys.argv) > 2:  # makes sure more than 1 parameter is supplied
    if sys.argv[1] == "-a":
        Fatui(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-r":
        ImToFile(sys.argv[2])
else:  # print a message of how to use the program
    print("file2bmp55 by koleq (C)2021\n\n" +
          "# How to use\n\n" +
          "python main.py input_file_path output_file_path.bmp\n\n" +
          "## input can be any file that you want\n" +
          "## output has to be .bmp")


