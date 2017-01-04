#/usr/bin/env python3
# -*- coding:utf-8 -*-
try:
    import tinify
except ImportError:
    print('you need to install tinify first, try \'pip(3) install --upgrade tinify\'')
    exit()
import os
import re

source_folder = '/Users/xxx/Desktop/icon/'
target_fodler = '/Users/xxx/Desktop/tinypng/'
def get_files():
    pattern = re.compile(r'.*\.(jpg|png)$')
    target_files = [f for f in os.listdir(source_folder) if pattern.match(f)]
    return target_files

def compress(file_list):
    if not os.path.exists(target_fodler):
        os.mkdir(target_fodler)
    for f in file_list:
        print('shrank ', f, '...')
        source = tinify.from_file(source_folder + f)
        source.to_file(source_folder + 'tinypng/' + f)

if __name__ == '__main__':
    print('compress with tinypng...')
    key = 'replace your own key here'
    tinify.key = key
    files = get_files()
    compress(files)
