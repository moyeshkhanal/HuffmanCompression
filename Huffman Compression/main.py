from HuffmanCompression import *

def main():
    huffman = HuffmanCompression("testFile.txt")
    huffman.makeFrequency()
    huffman.getBinary(huffman.makeTree())

    x = 3

main()