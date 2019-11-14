from TreeNode import *
import pickle
from WriteBitFile import *
from ReadBitFile import *
#https://wiki.python.org/moin/UsingPickle

class HuffmanCompression:

    def __init__(self, filename):
        self.codesDictionary = {}
        self.filename = filename
        self.freq = {}
        self.charToCode = {}
        self.bits = 0

    def __getBinaryHelper(self, root, code):
        if root == None:
            return
        if root.char != "Value":
            self.codesDictionary[code] = root.char
            self.charToCode[root.char] = code
            return
        self.__getBinaryHelper(root.left, code + "0")
        self.__getBinaryHelper(root.right, code + "1")

    def getBinary(self, parent):
        root = (parent)
        code = ""
        self.__getBinaryHelper(root, code)

    def makeFrequency(self):
        with open(self.filename, "r") as line:
            for word in line:
                for c in word:
                    self.bits += 1
                    # starts the freq count at 1, so we can add things later
                    if c not in self.freq:
                        self.freq[c] = 1
                    else:
                        self.freq[c] = self.freq[c] + 1
    def makeTree(self):
        freqDic = self.freq
        minQueue = []
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
                index = 0
                while minQueue[index].frequency < parent.frequency:
                    index += 1
                    if index == len(minQueue):
                        break
                minQueue.insert(index, parent)
        return parent

    def compress(self):
        w = WriteBitFile("testFile2.txt.m")
        w.writeUInt(self.bits)
        codedChr = self.codesDictionary
        pickle.dump(codedChr, w.outfile)
        # curBit = ""
        with open(self.filename, "r") as line:
            for word in line:
                for char in word:
                    if char in self.charToCode:
                        curBit = self.charToCode[char]
                        for b in curBit:
                            w.writeBit(int(b))
        # w.outfile
        # self.filename.close()
        w.close()
        #uINT file byte size then Pickle then the compressed file

    def deCompress(self):
        r = ReadBitFile("testFile2.txt.m")
        w = WriteBitFile("testFile2_decompressed.txt")
        byteSize = r.readUInt()
        codedChr = pickle.load(r.infile)
        print(codedChr)
        bitStr = ""
        for i in range(byteSize):
            bit = r.readBit()
            bitStr += str(bit)
            if bitStr in codedChr:
                charToWrite = codedChr[bitStr]
                w.writeUByte(ord(charToWrite))
                bitStr = ""
        w.close()
        r.close()
