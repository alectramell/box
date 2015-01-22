#!/usr/bin/python

import os

gsearch = str('''
GOOGLE=$(zenity --entry --title="www.Google.com" --text="Search: ") && sensible-browser --new-window=https://www.google.com/?gws_rd=ssl#q=$GOOGLE && clear
''')

os.system(gsearch)
