#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .gui import ShowGUI
import sys


def Run():
    print(sys.path)
    print("I'm OK from git repo")
    ShowGUI()


if __name__ == '__main__':
    Run()
