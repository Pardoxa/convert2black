#!/usr/bin/env python3
from PIL import Image, ImageEnhance
import sys
import pdf2image

DPI = 200
FORMAT = 'png'
THREAD_COUNT = 8

def pdf2pli(path):
    img = pdf2image.convert_from_path(path, dpi=DPI, fmt=FORMAT, thread_count=THREAD_COUNT)
    return img

def get_img(path):
    if path.endswith(".pdf"):
        return pdf2pli(path)
    else:
        return [Image.open(path)]

def main():
    length = len(sys.argv)
    mode = "L"
    if length < 2:
        print("Usage: ./convert2black pathToImageOrPdf <mode>")
        print("mode is an optional parameter and can be for example L or 1 or filter")
        exit(0)
    elif length >= 3:
        mode = sys.argv[2]
    filename = sys.argv[1]

    print(filename)
    img = get_img(filename)
    if mode == "filter":
        for i in range(len(img)):
            filter = ImageEnhance.Color(img[i])
            img[i] = filter.enhance(0)
    else:
        for i in range(len(img)):
            img[i] = img[i].convert(mode)

    for i in reversed(range(len(img))):
        img[i].show()

if __name__ == '__main__':
    main()
