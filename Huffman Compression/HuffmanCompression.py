# Moyesh Khanal
# Gage Farmer
# HuffmanCompression.py
# 11/18/2019
#

from TreeNode import *
import pickle
from WriteBitFile import *
from ReadBitFile import *

class HuffmanCompression:

    def __init__(self, filename):
        # initialize the codes to character dictionary
        self.codesDictionary = {}
        # name of the file to decompress
        self.filename = filename
        # frequency of character dictionary
        self.freq = {}
        # initialize the Character to code dictionary
        self.charToCode = {}
        self.bits = 0
        # name of the outfile
        self.outfile = ""
        # make the frequency
        self.__makeFrequency()

    def __getBinaryHelper(self, root, code):
        # if the parent is None return
        if root == None:
            return
        # if the root character is not the value we are looking for
        if root.char != "Value":
            # add code as key and character as value
            self.codesDictionary[code] = root.char
            # add character as key and code as value
            self.charToCode[root.char] = code
            # return out of the recursion
            return
        # do the left of the tree, add 0 as the binary code
        self.__getBinaryHelper(root.left, code + "0")
        # do the right of the tree, add 1 as the binary code
        self.__getBinaryHelper(root.right, code + "1")

    def __getBinary(self, parent):
        # make root the parent
        root = parent
        # empty code string
        code = ""
        # call _getBinaryHelper with root and empty code string
        self.__getBinaryHelper(root, code)

    def __makeFrequency(self):
        # Open the file as line
        with open(self.filename, "r") as line:
            # for each word in that line
            for word in line:
                # for each charcter in that word
                for c in word:
                    # add one to the number of bits
                    self.bits += 1
                    # starts the freq count at 1, so we can add things later
                    if c not in self.freq:
                        self.freq[c] = 1
                    else:
                        self.freq[c] = self.freq[c] + 1
        # call makeTree after the frequency is made
        self.__makeTree()
    def __makeTree(self):
        # set freqDic to the frequency dictionary instance variable
        freqDic = self.freq
        # make a queue list
        minQueue = []
        # set parent to none
        parent = None

        # creates queue with the shortest frequencies first
        while freqDic:
            minChar = None
            minVal = min([v for c, v in freqDic.items()])
            for c, v in freqDic.items():
                if v == minVal:
                    minChar = c
            minQueue.append(TreeNode(minChar, minVal))
            freqDic.pop(minChar)

        # creates tree, returns parent
        while len(minQueue) > 1:
            newMin = minQueue[0].frequency + minQueue[1].frequency
            parent = TreeNode("Value", newMin, minQueue[0], minQueue[1])
            minQueue.pop(0)
            minQueue.pop(0)
            # if the length of the queue is 1 we know what it does next,
            # so we do it here instead of doing another loop, then exit
            if len(minQueue) == 1:
                newMin = minQueue[0].frequency + parent.frequency
                if parent.frequency > minQueue[0].frequency:
                    parent = TreeNode("Value", newMin, minQueue[0], parent)
                else:
                    parent = TreeNode("Value", newMin, parent, minQueue[0])

            else:
                # else make the index at the beginning
                index = 0
                # while the frequency of the character at index is less than parent's frequency
                while minQueue[index].frequency < parent.frequency:
                    # increase the index by one
                    index += 1
                    # if the index is now length of queue
                    # break from the loop
                    if index == len(minQueue):
                        break
                # insert parent at the index
                minQueue.insert(index, parent)
        # call getBinary with parent
        self.__getBinary(parent)
        # return parent

    def compress(self):
        # get the name of the outfile as the name of the file and .m as the extension
        self.outFile = self.filename + ".m"
        # make the outfile writable
        w = WriteBitFile(self.outFile)
        # make the header with number of bits in the original file and the dictionary as a pickle dump
        w.writeUInt(self.bits)
        codedChr = self.codesDictionary
        pickle.dump(codedChr, w.outfile)
        # with the file open as line to compress
        with open(self.filename, "r") as line:
            # for each word in line
            for word in line:
                # for character in word
                for char in word:
                    # if the character is in the dictionary
                    if char in self.charToCode:
                        # make curbits the binary representation of that character
                        curBit = self.charToCode[char]
                        for b in curBit:
                            # write each bit in curbit in the writeable file
                            w.writeBit(int(b))
        # close the writable file
        w.close()

    def deCompress(self):
        # r as read the outfile that was compressed
        r = ReadBitFile(self.outFile)
        # outfile as filename + _decompressed.txt extension after decompressing
        w = WriteBitFile(self.filename + "_decompressed.txt")
        # the first UInt from the file is the byte size from the original file
        byteSize = r.readUInt()
        # get the dictionary from the header
        codedChr = pickle.load(r.infile)
        # the bitstring is empty string
        bitStr = ""
        i = 0
        # while i is not equal to the original byte size
        while i != byteSize:
            # read each bit
            bitStr += str(r.readBit())
            # check if the collection of bits is in the dictionary
            if bitStr in codedChr:
                # increase i by one as we find the byte
                i += 1
                # write the letter corresponding to the byte
                charToWrite = codedChr[bitStr]
                w.writeUByte(ord(charToWrite))
                # make bitStr to empty string
                bitStr = ""
        # close the two open files
        w.close()
        r.close()
