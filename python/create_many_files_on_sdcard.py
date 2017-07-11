# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess

local_file_path = ''
dir = ''

def mkfiles():
    subprocess.check_output(['adb', 'shell', 'mkdir', dir])
    for i in range(10000):
        subprocess.call(['adb', 'push', local_file_path, dir +'/' + str(i) + '.gif'])

if __name__ == '__main__':
    try:
        r = len(subprocess.check_output(['adb', 'devices']).decode('utf-8').split('\n'))
        if r == 4:
            mkfiles()
            pass
        elif r < 4:
            print('No device connected!')
        elif r > 4:
            print('More than one devices connected!')
    except Exception as e:
        pass
        exit(1)
