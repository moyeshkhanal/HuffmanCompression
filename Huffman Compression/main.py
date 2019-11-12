from HuffmanCompression import *

def main():
    huffman = HuffmanCompression("testFile.txt")
    huffman.makeFrequency()
    huffman.getBinary(huffman.makeTree())
    huffman.compress()
    print(huffman.deCompress())

    x = 3

main()