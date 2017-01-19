#!usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import PIL.Image as Image

grey2char = ['*', '#', '$', '%', '&', '?', '*', 'o', '/', '{', '[', '(', '|', '!', '^', '~', '-',
             '_', ':', ';', ',', '.', '`', ' ']
count = len(grey2char)


def convert_file_to_text(file):
    gray_image_file = file.convert('L')  # 转灰度
    result = ''
    for h in range(0, gray_image_file.size[1]):  # height
       result += '*'
       for w in range(0, gray_image_file.size[0]):  # width
           gray = gray_image_file.getpixel((w, h))
           result += grey2char[int(gray / (255 / (count - 1)))]
       result += '\t\n'
    return result


def save_to_file(text="error", file_path="~/Desktop/output.txt"):
    output_file = open(file_path, 'w')
    output_file.write(text)
    output_file.close()
    print('saved successfully')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('scale')
    parser.add_argument('out')

    args = parser.parse_args()
    img_path = args.file
    scale = float(args.scale)
    output = args.out

    image_file = Image.open(img_path)
    x = int(image_file.size[0] * scale)
    y = int(image_file.size[1] * 0.55 * scale)
    print(x, y)
    image_file = image_file.resize((x, y), Image.ANTIALIAS)
    image_text = convert_file_to_text(image_file)
    save_to_file(image_text, output)
