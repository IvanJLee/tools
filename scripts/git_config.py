# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess

name = 'Ivan'
email = 'lijundut@foxmail.com'

def main():
    subprocess.call(['git', 'user.name', name])
    subprocess.call(['git', 'user.email' email])

if __name__ == '__main__':
    main()
