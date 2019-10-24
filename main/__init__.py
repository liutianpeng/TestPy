#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os


def Run():
    print(os.path.abspath("../"))
    cmd = os.path.join(os.path.abspath("../"), "bin/ztm-tools.exe")
    os.system(cmd)
    return


if __name__ == '__main__':
    Run()
