#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
from . import server


def Run(baseDir):
    cmd = os.path.join(baseDir, "bin/ztm-tools.exe")
    os.popen(cmd)

    server.StartServer(19001)
    return

if __name__ == '__main__':
    Run("./")
