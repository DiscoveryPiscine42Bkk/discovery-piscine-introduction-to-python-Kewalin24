import sys #ค้องrunในbushผลถึงจะออกตามโจทย์นี้

if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")