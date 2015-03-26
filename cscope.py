#!/usr/bin/env python
# coding: utf-8

import os
import sys


find = r'E:\OS\Windows\Soft\App\GnuWin32\GnuWin32\bin\find.exe'
cscope = r'E:\Soft\cscope\bin\cscope.exe'


def cscope(dirs):
    print(dirs)
    cmd = '{} {} -type f -name "*.[ch]" -fprint cscope.files'.format(
        find, dirs)
    print(cmd)
    os.system(cmd)

    cmd = '{} -bqf .cscope.out'.format(cscope)
    print(cmd)
    os.system(cmd)


def main():
    if (len(sys.argv) == 1):
        dirs = ['.']
    else:
        # 统一使用‘/’路径分隔符
        dirs = [os.path.abspath(e).replace('\\', '/') for e in sys.argv[1:]]
        dirs = ' '.join(dirs)

    cscope(dirs)

if __name__ == "__main__":
    main()
