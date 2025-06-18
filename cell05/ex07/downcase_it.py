#!/usr/bin/python3
import sys #ต้องrunในbushผลถึงจะออกตามโจทย์นี้

if len(sys.argv) == 2:
    print(sys.argv[1].lower())
else:
    print("none")