from HuffmanCompression import *

def main():
    huffman = HuffmanCompression("pickleTest.txt")
    # huffman.makeFrequency()
    # huffman.getBinary(huffman.makeTree())
    huffman.compress()
    huffman.deCompress()

    x = 3

main()