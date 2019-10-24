#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os


def Run(baseDir):
    cmd = os.path.join(baseDir, "bin/ztm-tools.exe")
    os.popen(cmd)
    print("return")
    return


if __name__ == '__main__':
    Run("./")
