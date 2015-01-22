#!/usr/bin/python

import os

os.system("clear")

os.system("cd ~/ && git clone http://github.com/alectramell/box.git")

os.system("clear")

boxid = raw_input("BOX ID: ")

boxname = str("~/box/files/" + boxid + "/")

os.system("gnome-open " + boxname)

os.system("clear")
