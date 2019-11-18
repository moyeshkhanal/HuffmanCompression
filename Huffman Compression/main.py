# Moyesh Khanal
# Gage Farmer
# main.py
# 11/18/2019
#
from HuffmanCompression import *
import sys

def main(argv):
    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = input("Enter Filename: ")
    huffman = HuffmanCompression(filename)
    huffman.compress()
    huffman.deCompress()

if __name__ == '__main__':
    main(sys.argv)